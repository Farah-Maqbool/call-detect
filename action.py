import smtplib
from email.mime.text import  MIMEText

def send_email_alert(text: str, to_email: str = "taerahsmile23@gmail.com"):
    'send email alert'

    msg = MIMEText(f'Threat Detected:\n\n{text}')
    msg["Subject"]  = "Alert: Threat Detected"
    msg['From'] = 'alert-system@example.com'
    msg['To'] = to_email

    with smtplib.SMTP('localhost') as server:
        server.send_message(msg)

        