import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import socket
import datetime
e = datetime.datetime.now()

hostname = socket.gethostname()
#date = f"{e.day}.{e.month}.{e.year}_{e.hour}:{e.minute}:{e.second}"
date = f"{e.day}.{e.month}.{e.year}_{e.hour}:{e.minute}"

fromaddr = 'manasa.intern@phonepe.com'
toaddr = 'manasaman7@gmail.com'
subject = 'Database_Schema_alert'
content = 'The database schema has been changed,the below attached file contains the changes'

msg = MIMEMultipart() # saying the module to load our data
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)

filename = f"{hostname}_{date}.txt"
with open(filename, 'r') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))
    part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect("smtp.gmail.com",587)
server.starttls()
#server.login(fromaddr, 'anvlsnjyxarsvfoc')
server.login(fromaddr, 'mooqppareshpesjm')
server.send_message(msg, fromaddr, toaddr)

server.quit()

