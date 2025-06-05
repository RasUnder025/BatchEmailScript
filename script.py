import cv2
import pandas as pd

# the csv file of attendees
part_df = pd.read_csv('./registrations.csv')
# the certificate template as image
template = cv2.imread('template.png');

# text font
font = cv2.FONT_HERSHEY_TRIPLEX
# origin position in certificate
org = (563, 554)
# text fontScale
fontScale = 2
# black color in RGB
color = (0, 0, 0)
# line thickness of 2 px
thick = 1
# total number of entries
count = part_df.shape[0]

for index in range(count):
    # the USN column in csv file is 3
    usn = part_df.iloc[index, 3]
    # the name column in csv file is 2
    name = str(part_df.iloc[index, 2])
    # the library function to draw on file
    cv2.putText(template, name.upper(), org, font, fontScale, color, thick, cv2.LINE_AA);
    cv2.imwrite(f'.\participants\{usn}.png', template);
    print('Processing cert: {}/{}'.format(index+1, count))
    template = cv2.imread('template.png');

import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# app password from Google accounts (2FA)
gmail_pass = "xxxx xxxx xxxx xxxx"

# the 'from' email address
user = "example@gmail.com"

# the standard SMTP host
host = "smtp.gmail.com"

# the standard port for SSL
port = 465

# who are we sending this email to?
to = "example@gmail.com"

# what is our subject line?
subject = "FILL THE SUBJECT"

# what is the body of the email?
body = """Dear sir/madam,
FILL THE BODY
Best regards,
example."""

# what is the name of the file path we want to attach?
filename = "\\template.png"

# attach the file
if os.path.exists(filename):  # ensure file exists
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

def send_email(to, subject, body, filename):
    # create message object
    message = MIMEMultipart()

    # add in header
    message['From'] = Header(user)
    message['To'] = Header(to)
    message['Subject'] = Header(subject)

    # attach message body as MIMEText
    message.attach(MIMEText(body, 'plain', 'utf-8'))

    # locate and attach desired attachments
    att_name = os.path.basename(filename)
    with open (filename, 'rb') as _f:
        att = MIMEApplication(_f.read(), _subtype="txt")
    _f.close()
    att.add_header('Content-Disposition', 'attachment', filename=att_name)
    message.attach(att)

    # setup email server
    server = smtplib.SMTP_SSL(host, port)
    server.login(user, gmail_pass)

    # send email and quit server
    server.sendmail(user, to, message.as_string())
    server.quit()

send_email(to, subject, body, filename) # attempt an initial test case
for index in range(count): # iteration for all the emails in csv
    # email address in cvs file is column 1
    to = part_df.iloc[index, 1]
    filename = "\\participants\\{}.png".format(part_df.iloc[index, 3])
    send_email(to, subject, body, filename)
print("Emails Successfully sent.");
