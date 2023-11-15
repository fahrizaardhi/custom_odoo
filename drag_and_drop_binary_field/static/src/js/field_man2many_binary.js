/** @odoo-module **/
import {registry} from "@web/core/registry";
import {Many2ManyBinaryField} from "@web/views/fields/many2many_binary/many2many_binary_field";
import {onMounted} from "@odoo/owl";

export class FieldMany2manyBinaryFileDragAndDrop extends Many2ManyBinaryField {
    setup() {
        super.setup();
        onMounted(() => {
            this.el = this.__owl__.bdom.parentEl;
            this.el.addEventListener("drop", (ev) => this._onDropDown(ev));
            this.el.addEventListener("dragenter", this._disableDefaultDragEvents);
            this.el.addEventListener("dragover", this._disableDefaultDragEvents);
            this.el.addEventListener("dragleave", this._disableDefaultDragEvents);
        });
    }

    _onDropDown(ev) {
        ev.preventDefault();

        if (ev.dataTransfer.items) {
            [...ev.dataTransfer.items].forEach((item, i) => {
                if (item.kind === "file") {
                    const file = item.getAsFile();
                    this.uploadData(file);
                }
            });
        } else {
            [...ev.dataTransfer.files].forEach((file, i) => {
                this.uploadData(file);
            });
        }
    }

    uploadData(file) {
        const customFileList = new DataTransfer();
        customFileList.items.add(file);
        const input = this.el.querySelector(".o_input_file");
        input.files = customFileList.files;
        const event = new Event("change");
        input.dispatchEvent(event);
    }

    _disableDefaultDragEvents(e) {
        e.preventDefault();
    }
}

registry
    .category("fields")
    .add("drag_and_drop_many2many_binary", FieldMany2manyBinaryFileDragAndDrop);
