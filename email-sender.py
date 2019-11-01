import smtplib
import os
import pyautogui
import time
import datetime

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

while 1:

    now = datetime.datetime.now()
    attachments_path = ""
    my_email = ""
    my_password = ""
    send_frequency_mins = 60
    send_frequency_seconds = 60 * send_frequency_mins

    # Take a screenshot and save it
    screenshot = pyautogui.screenshot()
    screenshot.save(attachments_path + "screenshot.png")

    # Sleep to allow screenshot processing
    time.sleep(1)

    # Construct the email
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Update From PC"
    msg.attach(MIMEText("See attachment for update."))

    # And attach the screenshot we just took
    f = open(attachments_path+"screenshot.png", 'rb').read()
    attachment = MIMEImage(f, name=os.path.basename(attachments_path + "screenshot.png"))
    msg.attach(attachment)

    # Now send the email
    smtp = smtplib.SMTP('smtp.gmail.com')
    smtp.starttls()
    smtp.login(my_email, my_password)
    smtp.sendmail(my_email, my_email, msg.as_string())
    smtp.close()

    # Log it
    print(now.strftime("%Y-%m-%d %H:%M:%S") + " sent email")

    # Now sleep until it's time to send an email again
    time.sleep(send_frequency_seconds)
