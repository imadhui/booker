import os
import wget
import urllib.parse
from fastapi import FastAPI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def decode_url(url):
    return urllib.parse.unquote(url)

def downloadBook(url):
    file_name = wget.download(url)
    book_name = decode_url(file_name)
    os.rename(file_name, book_name)
    return book_name

def sendmail(filepath):
    fromaddr = "bileeveit@gmail.com"
    toaddr = "madhuofficialcontact@icloud.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Subject of the Mail"

    # string to store the body of the mail
    body = "Brought to you by imadhui's send2kindle service!!!"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename =  os.path.basename(filepath)
    attachment = open(filepath, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "qgmckppweruntuwx")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()






# Server

app = FastAPI()

@app.get("/send2kindle")
def hello(book_url: str):
    downloadBook(book_url)
    return 'Hello ' + book_url + '!'
