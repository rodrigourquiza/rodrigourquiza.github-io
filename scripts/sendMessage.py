import datetime as dt
import js
import locale
from pyodide import create_proxy
import smtplib
import email
import email.mime
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
    feedbackElement = js.document.getElementById('feedback')
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
            feedbackElement.innerHTML = f"Error: {ex.args} {os.getcwd()}"
        #Encoders.encode_base64(part)
        #part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
        #msg.attach(part)

    try:
        #https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
        step=0
        server = smtplib.SMTP("smtp.gmail.com", 587)
        step=1
    #    server.ehlo()
        step=2
    #    server.starttls()
        step=3
    #    server.ehlo()
        step=4
    #    server.login(username, passwd)
        step=5
    #    server.sendmail(username, to, msg.as_string())
        step=6
    #    feedbackElement.innerHTML = "Successfully sent email"
    except smtplib.SMTPException:
        feedbackElement.innerHTML = "Error: unable to send email"
    except Exception as ex:
        ex.args
        feedbackElement.innerHTML = f"{step} -- Error: {ex.args}"
    finally:
        #server.close()
        pass

def sendMessage(event, *args, **kwargs):

    #print('args:', args)
    #print('kwargs:', kwargs)

    #// get the feedback div element so we can do something with it.
    feedbackElement = js.document.getElementById('feedback')

    originalLocale = locale.getlocale(category=locale.LC_CTYPE)
    lang = js.document.documentElement.lang
    locale.setlocale(category=locale.LC_CTYPE,locale=lang)
  
    js.console.log(f'args: {args}')
    js.console.log(f'kwargs: {kwargs}')

    match(lang):
        case 'en-us':
            name = 'name'
            email = 'e-mail'
            message = 'message'
            dateTime = 'date time'
            language = 'language'
            locale.setlocale(category=locale.LC_CTYPE,locale='en')
        case 'es-pe':
            name = 'nombre'
            email = 'e-mail'
            message = 'mensaje'
            dateTime = 'fecha hora'
            language = 'idioma'
            locale.setlocale(category=locale.LC_CTYPE,locale='es')

    from_email = Element('mail').element.value
    
    text = f"{name}:  {Element('name').element.value}"
    text = f"{text}; {email}:  {from_email}"
    text = f"{text}; {message}:  {Element('msg').element.value}"
    text = f"{text}; {dateTime}:  {dt.datetime.now().strftime('%H:%M:%S on %A %B %d, %Y')}"
    text = f"{text}; {language}:  {lang}"
  
    mail(from_email, receiver, "test", text)
   
    #print('text:', text)
    js.console.log(f'text: {text}')

    #// stop the form from doing the default action.
    event.preventDefault();
    #// set the contents of our feedback element to a message letting the user know the form was submitted successfully. Notice that we pull the name that was entered in the form to personalize the message!
    match(lang):
        case 'en-us':
            #feedbackElement.innerHTML = 'Hello '+ formElement.user_name.value +'! Thank you for your message. We will get back with you as soon as possible!';
            pass
        case 'es-pe':
            #feedbackElement.innerHTML = '¡Hola '+ formElement.user_name.value +'! Gracias por tu mensaje. ¡Nos pondremos en contacto contigo lo antes posible!';
            pass
    #// make the feedback element visible.
    feedbackElement.style.display = "block";
    #// add a class to move everything down so our message doesn't cover it.
    js.document.body.classList.toggle('moveDown');

    Element('pyFeedback').element.style.display = "block"
    #Element('pyFeedback').element.innerText = text
    pyscript.write('pyFeedback', text)
    locale.setlocale(category=locale.LC_CTYPE,locale=originalLocale)

#// get the form so we can read what was entered in it.
formElement = js.document.forms[0];
formElement.addEventListener('submit', create_proxy(sendMessage));