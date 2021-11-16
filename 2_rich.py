import smtplib
from config import from_email, password, to
from email.message import EmailMessage


def send_mail():
    msg = EmailMessage()
    subject = "This is HTML mail 6"
    html_body = '''
    This is <span style='color:red'>colorful</span> body.
    '''
    msg["Subject"] = subject
    msg['From'] = from_email
    msg['To'] = to

    msg.set_content(html_body, subtype='html')
    # FALLBACK
    msg.add_alternative("This is plain text", subtype='text')

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(from_email, password)
        smtp.send_message(msg)
        print("sent")


if __name__ == '__main__':
    send_mail()
