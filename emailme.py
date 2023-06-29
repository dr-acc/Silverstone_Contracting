## email

import smtplib
import ssl
from email.message import EmailMessage
import os

PORT = 465  # For SSL
SMTP_SERVER = "smtp.gmail.com"
SENDER = "justferfunan@gmail.com"  # Enter your address
RECEIVER = "justferfunan@gmail.com"  # Enter receiver address
PASSWORD = os.environ.get('SMTPPASSWORD')
message = """\
Subject: Hi there

This message is sent from Python."""

ssl_context = ssl.create_default_context()


def send_an_email(port=PORT, smtp_server=SMTP_SERVER, sender=SENDER, receiver=RECEIVER, password=PASSWORD, context=ssl_context, msg=message):

    mail_to_send = EmailMessage()
    mail_to_send.set_content(msg)
    mail_to_send['Subject'] = "Silverstone Form Submission"
    mail_to_send['From']=sender
    mail_to_send['To']=receiver

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        server.send_message(mail_to_send)
    

if __name__ == "__main__":
    send_an_email()