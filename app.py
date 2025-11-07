import smtplib
import ssl
from email.message import EmailMessage
import time
import schedule
from dotenv import load_dotenv
import os
import pytz
from datetime import datetime


def check_palindrome_time():
    tz = pytz.timezone('Africa/Lagos')
    curr_time = datetime.now(tz).strftime("%H:%M")
    curr_time = curr_time.replace(":", "")

    curr_time = str(curr_time)

    if curr_time == curr_time[::-1]:
        send_email()

    else:
        print("Not a palindrome time.") 


def send_email():
    curr_time  = time.strftime("%H:%M", time.localtime())
    load_dotenv()

    email_sender = os.getenv("EMAIL_SENDER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_host = os.getenv("EMAIL_HOST")
    email_port = int(os.getenv("EMAIL_PORT"))
    email_receiver = os.getenv("EMAIL_RECEIVER")
    
    subject = "Palindrome Time Alert!"
    body = f"""
        Hey there,

        Welcome to THE REST OF YOUR LIFE!
        
        The current time {curr_time} is a palindrome!
        Best,
        Your Palindrome Notifier
        """
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg.set_content(body)


    context = ssl.create_default_context()

    with smtplib.SMTP(email_host, email_port) as server:
        server.starttls(context=context)
        server.login(email_sender, email_password)
        server.send_message(msg)
        print("Email sent successfully!")

schedule.every().minute.do(check_palindrome_time)

while True:
    schedule.run_pending()
    time.sleep(1)
