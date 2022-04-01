# =================================================================================================================
# FUNCTIONS BELOW SEND EMAIL ALERTS TO TEAM MEMBERS
# =================================================================================================================

import smtplib
from email.message import EmailMessage

import os
from dotenv import load_dotenv

load_dotenv()

sending_email_address = os.environ['sending_email_address']
password = os.environ['password']
receiving_email = os.environ['receiving_email']

msg = EmailMessage()
msg['Subject'] = "" # to be set when function runs
msg['From'] = sending_email_address
msg['To'] = receiving_email


def send_new_address_email_alert(new_address):
    msg['Subject'] = "NEW ADDRESS PATTERN DETECTED"
    msg.set_content(f"""\
        <!doctype html>
        <html>
        <head></head>
        <body style="line-height:30px;font-size:30px;">            
            <p style = "font-weight:normal;font-size:30px;">New address type is received</p>             
            
        <p style = "font-weight:normal;font-size:30px;">Address: {new_address}</p>
            </body>
            </html>
    """,subtype ='html'
    )
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sending_email_address, password)
            smtp.send_message(msg)
            print("email sent ")
    except:
        print("Could not send email. Please make sure the email and password are properly set in the \
            .env file the email account settings are done")

def send_error_email_alert(error):
    msg['Subject'] = "ERROR HAS OCCURED"
    msg.set_content(f"""\
        <!doctype html>
        <html>
        <head></head>
        <body style="line-height:30px;font-size:30px;">            
            <p style = "font-weight:normal;font-size:30px;">New address type is received</p>             
            
        <p style = "font-weight:normal;font-size:30px;">Address: {error}</p>
            </body>
            </html>
    """,subtype ='html'
    )
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sending_email_address, password)
            smtp.send_message(msg)
            print("email sent ")

    except:
        print("Could not send email. Please make sure the email and password are properly set in the \
                .env file and the email account settings are done")