import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import os  

username = "tmannathp@gmail.com"
passwd = "ZAQ!xsw2cde3vfr4"
receiver = "tracy.mann1@retailbusinessservices.com"

def mail(from_email, to, subject, text, attach=None):
    #attach="./index-en.html"
    #// get the feedback div element so we can do something with it.
    msg = MIMEMultipart()

    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text)) 
    if attach != None:
        part = MIMEBase('application', 'octet-stream')
        try:
            part.set_payload(open(attach, 'rb').read())
        except Exception as ex:
            print(f"Error: {ex.args} {os.getcwd()}")
        #Encoders.encode_base64(part)
        #part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
        #msg.attach(part)

    try:
        #https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
        step=-1
        print(f"{step}")
        #server = smtplib.SMTP_SSL(None, timeout=120)
        server = smtplib.SMTP_SSL(None, timeout=180)
        #server = smtplib.SMTP_SSL(None, timeout=240)
        step=0
        print(f"{step}")
        #server = smtplib.SMTP("smtp.gmail.com", 587, username, timeout=120)
        #server = smtplib.SMTP_SSL("smtp.gmail.com", 465, username, timeout=120)
        #server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        #server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=120)
        server.connect("smtp.gmail.com", 465)
        #server = smtplib.SMTP_SSL("smtp.gmail.com", 465, username, timeout=240)
        step=1
        print(f"{step}")
        server.ehlo()
        #step=2
        #print(f"{step}")
        #server.starttls()
        #step=3
        #print(f"{step}")
        #server.ehlo()
        step=4
        print(f"{step}")
        server.login(username, passwd)
        step=5
        print(f"{step}")
        server.sendmail(username, to, msg.as_string())
        step=6
        print(f"{step}")
        print("Successfully sent email")
    except smtplib.SMTPException as ex:
        print(f"Error: unable to send email -- {ex}")
    except Exception as ex:
        ex.args
        print(f"{step} -- Error: {ex.args}")
    finally:
        print("closed")
        server.close()
        pass

mail('from_email', username, 'subject', 'text')