import smtplib
from email.mime.text import MIMEText
import os
import pyautogui
from config import *




def send_message(message):
    sender ='artykovh@gmail.com'
    to_send = 'atabekis2006@gmail.com'
    password_email = password

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password_email)
        msg = MIMEText(message)
        msg['Subject'] = 'Click Me'
        server.sendmail(sender, to_send, msg.as_string())
        return 'Message sent'
    except Exception as e:
        return f'{e} Error'
    

    

def main():
    msg = input("Enter message: ")
    print(send_message(msg))

    
    


if __name__ == '__main__':
    main()
