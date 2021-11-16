import smtplib
from config import from_email, password, to
from email.message import EmailMessage


def send_mail():
    msg = EmailMessage()
    subject = 'This is HTML mail 7'
    plain_body = 'This is plain text'
    html_body = '''
    This is <span style='color:red'>colorful</span> body.
    '''
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to
    msg.set_content(plain_body, subtype='text')
    msg.add_alternative(html_body, subtype='html')

    # Text or text like file
    with open('data.csv', 'r') as f:
        msg.add_attachment(f.read(),
                           filename='data.csv'
                           )

    # Image file
    with open('stock-image.jpeg', 'rb') as f:
        msg.add_attachment(f.read(),
                           maintype='image',
                           subtype='jpeg',
                           filename='stock-image.jpeg'
                           )

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(from_email, password)
        smtp.send_message(msg)
        print('sent')


if __name__ == '__main__':
    send_mail()
