#!/usr/bin/python3
import hashlib, json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


date = datetime.now().strftime("%B %d, %Y  %I:%M %p")
body = '''
<html>
  <body>
    <h2>Following contains the integrity status of target files: </h2>
    <br>
  </body>
</html>
'''


BUF_SIZE = 65536

# add path to baseline.json
with open('', 'r') as baseline:
    data = json.load(baseline)

    for path in data:
        with open(path, 'rb') as f:
            content = f.read(BUF_SIZE)
            hash = hashlib.sha256(content)
            hash = hash.hexdigest()
            
            baseline_hash = data[path]

            if(hash == baseline_hash):
                body += f"<h3>{path} - <strong>unchanged</strong></h3><br>"
            elif(hash != baseline_hash):
                body += f"<h3 style='color:red;'>{path} - <strong>INTEGIRTY COMPROMISED</strong></h3><br>"


    message = MIMEMultipart()
    message['To'] = "recipient's email address"
    message['From'] = "you email address"
    message['Subject'] = f"Integrity Check - {date}"
    message.attach(MIMEText(body, 'html'))


    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:

            s.starttls()

            s.login("your email address", "passcode")

            s.send_message(message)


    except Exception as e:
        print("unable to send mail - ", e)
