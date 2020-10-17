import json
import smtplib
import imaplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import email
import datetime

def send_mail_server():
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()

    return server

    
def from_config():
    infos = dict()
    infos['email'] = input("E-mail: ")
    infos['identity'] = input("Identity: ")

    file_content = json.dumps(infos)

    config = open(".from_config.json", 'w')
    config.write(file_content)
    config.close()
    print("File .from_config.json successfully created")

def send():
    print("Connecting with the server...")
    server = send_mail_server()
    
    print("Reading the sender configs...")
    file_configs = open('.from_config.json', 'r')
    from_config = json.load(file_configs)
    file_configs.close()
    
    file_configs = open('.to_config.json', 'r')
    print("Reading the receiver configs...")
    to_config = json.load(file_configs)
    file_configs.close()

    deadline = to_config['deadline']

    date = str(datetime.date.today())
    
    if int(deadline.split("/")[0]) < int(date.split("-")[0]) and int(deadline.split("/")[1]) < int(date.split("-")[1]) and int(deadline.split("/")[2]) < int(date.split("-")[2]):
        print("\033[1;31mDeadline expired\033[0;0m")
        return
    
    password = getpass.getpass(f"Password [{from_config['email']}]: ")
    print("Login...")
    server.login(from_config['email'], password)

    mens = MIMEMultipart()
    
    mens['From'] = from_config['email']
    mens['To'] = to_config['email']
    mens['Subject'] = to_config['subject']

    body = f"\n{from_config['identity']}"

    mens.attach(MIMEText(body, 'plain'))

    filename = f'{from_config["identity"]}.zip'

    attachment = open(filename,'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename={filename}")
    mens.attach(part)
    attachment.close()

    server.sendmail(from_config['email'], to_config['email'], mens.as_string())
    server.quit()
    print("File uploaded successfully.")
