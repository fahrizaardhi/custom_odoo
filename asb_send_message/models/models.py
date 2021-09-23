# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    # override fungsi button_confirm
    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        for order in self:
            # Jika user adalah anggota dari group purchase user 
            # dan po_double_validation = two_step
            # dan amount_total lebih besar atau sama dengan po_double_validation_amount
            if order.user_has_groups('purchase.group_purchase_user')\
                    and (order.company_id.po_double_validation == 'two_step'\
                        and order.amount_total >= self.env.company.currency_id._convert(
                            order.company_id.po_double_validation_amount, order.currency_id, order.company_id, order.date_order or fields.Date.today())):
                # memanggil fungsi send_massage()
               self.send_massage()
        return res

    # mengirim message
    def send_massage(self):
        # mendifinisikan record direct massage yang akan menerima pesan
        direct_massage = self.env.ref('asb_send_message.purchase_order_room')
        # mendefinisikan pesan yang akan dikirim
        body = "PO Create, please check! " + "<a href='#id=%s&model=purchase.order&'>%s</a>" % (self.id, self.name)
        for rec in direct_massage:
            # mengirim message
            rec.message_post(body=body, content_subtype='html', message_type='comment', subtype_xmlid='mail.mt_comment')
        return