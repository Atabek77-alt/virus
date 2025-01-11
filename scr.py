import pyautogui
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import os
from config import *


EMAIL_FROM = "artykovh@gmail.com"
EMAIL_TO = "atabekis2006@gmail.com"
password_email = password
screenshot_file = "screenshot.png"


pyautogui.screenshot(screenshot_file)


msg = MIMEMultipart()
msg['From'] = EMAIL_FROM
msg['To'] = EMAIL_TO
msg['Subject'] = "Скриншот экрана"
msg.attach(MIMEText("Вот ваш скриншот.", 'plain'))

with open(screenshot_file, "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(screenshot_file)}")
    msg.attach(part)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(EMAIL_FROM, password_email)
    server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

os.remove(screenshot_file)
print("Скриншот отправлен и файл удален.")


