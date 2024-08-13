import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
from encodings import aliases

# Menambahkan alias baru ke dalam dict
aliases.aliases.update(
    {
        "windows_874": "cp874",  # Menambahkan alias baru '874' untuk encoding 'cp874'
    }
)

# Detail email
subject = "Contoh Email dengan Encoding CP874"
body = "Ini adalah pesan email yang dikodekan menggunakan encoding CP874."
to_email = "fahrizaarkana21@gmail.com"
from_email = "fahrizaarkana21@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 465
username = "username"
password = "password"

# Buat objek MIMEMultipart
msg = MIMEMultipart()
msg["From"] = formataddr((str(Header("windows-874", "windows-874")), from_email))
msg["To"] = to_email
msg["Subject"] = Header(subject, "windows-874")

# Bungkus body dalam MIMEText dengan encoding yang sesuai
mime_text = MIMEText(body, "plain", "windows-874")
msg.attach(mime_text)

with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(username, password)
    server.sendmail(from_email, to_email, msg.as_string())


print("Email berhasil dikirim.")
