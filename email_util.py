import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()
passw = os.getenv("email_password")




def send_email(subject, body, sender, recipients):

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, passw)
        smtp_server.sendmail(sender, recipients, msg.as_string())



