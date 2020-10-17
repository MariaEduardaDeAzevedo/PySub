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


def receive_email_server():
    server = imaplib.IMAP4_SSL("imap.gmail.com", 993)

    return server


def to_config():
    infos = dict()
    infos['email'] = input("E-mail: ")
    infos['subject'] = input("Subject: ")
    has_deadline = input("Do you want to set a deadline? [y/n] ")
    if has_deadline.upper() == "Y":
        deadline = input("Deadline model DD/MM/YY: ")
        passed = False
        while not passed:
            try:
                if 0 < int(deadline.split('/')[0]) <= 29 and 0 < int(deadline.split('/')[1]):
                    passed = True
                elif int(deadline.split('/')[0]) > 29 and int(deadline.split('/')[1]) != 2:
                    passed = True
                else:
                    passed = False
                    print("Deadline model is wrong")
                    deadline = input("Deadline model DD/MM/YY: ")

            except:
                passed = False
                print("Deadline model is wrong")
                deadline = input("Deadline model DD/MM/YY: ")

        infos['deadline'] = deadline

    file_content = json.dumps(infos)

    config = open("../send/.to_config.json", 'w')
    config_here = open(".to_config.json", 'w')
    config.write(file_content)
    config_here.write(file_content)
    config.close()
    config_here.close()
    print("File .to_config.json successfully created")
    readme = open('../send/README.md', 'a')
    content = f'\nE-mail:{input("E-mail specification: ")}\nIdentify: {input("Identify specification: ")}'
    readme.write(content)
    readme.close()

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
    deadline = from_config['deadline']

    date = str(datetime.date.today())
    
    if int(deadline.split("/")[0]) < int(date.split("-")[0]) and int(deadline.split("/")[1]) < int(date.split("-")[1]) and int(deadline.split("/")[2]) < int(date.split("-")[2]):
        print("\033[1;31mDeadline expired\033[0;0m")
        return

    file_configs.close()
    file_configs = open('.to_config.json', 'r')
    print("Reading the receiver configs...")
    to_config = json.load(file_configs)
    file_configs.close()
    
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
    server.logout()
    print("File uploaded successfully.")

def get_received():
    server = receive_email_server()
    file_configs = open('.to_config.json', 'r')
    print("Reading the receiver configs...")
    to_config = json.load(file_configs)
    file_configs.close()
    password = getpass.getpass(f"Password [{to_config['email']}]: ")
    server.login(to_config['email'], password)
    server.select()
    
    status, data = server.search(None, 'SUBJECT', to_config['subject'])

    received_list = open("RECEIVED.txt", 'a')
    error_list = open("ERROR.txt", 'a')

    for num in data[0].split():
        typ, d = server.fetch(num, '(RFC822)')
        mes = email.message_from_bytes(d[0][1])

        identify = ""
        from_email = mes['from']

        if mes.is_multipart():
            for part in mes.get_payload():
                if part.get_content_type() == "application/octet-stream":
                    identify = part.get_filename().split(".")[0]
                    try:
                        file_received = open(f'files/{identify}.zip', 'wb')
                        print(f"\033[1;32m{identify}\033[0;0m")
                        file_received.write(part.get_payload(decode=True))
                        file_received.close()
                        received_list.write(f"{identify} - {from_email}\n")
                    except Exception as error:
                        error_list.write(f"\033[1;31m{from_email['email']}\033[0;0m\n")
                        print(f"{identify}")

    received_list.close()
    error_list.close()
    server.close()
    server.logout()