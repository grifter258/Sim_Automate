import smtplib
from email.mime.text import MIMEText
from password import PASS
from password import PASS2

def send_email(subject, body, sender, recipients):

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, PASS)
        smtp_server.sendmail(sender, recipients, msg.as_string())


def send_email_2(subject, body, sender, recipients):

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, PASS2)
        smtp_server.sendmail(sender, recipients, msg.as_string())



