import email
import smtplib
from email.mime.text import MIMEText

def send_email(email,height,average_height):
    from_email = "moyalshimon@yahoo.com"
    from_password = "sismashelyahoo"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s.<strong>, the average height is %s" % (height, average_height)
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To']= to_email
    msg['From'] = from_email

    yahoo = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    yahoo.ehlo()
    yahoo.starttls()
    yahoo.login(from_email, from_password)
    yahoo.send_message(msg)
