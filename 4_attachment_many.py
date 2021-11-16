import smtplib
from config import from_email, password, to
from email.message import EmailMessage
import mimetypes


def send_mail():
    msg = EmailMessage()
    subject = 'This is HTML mail 2'
    plain_body = 'This is plain text'
    html_body = '''
    This is <span style='color:red'>colorful</span> body. 
    '''
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to
    msg.set_content(plain_body, subtype='text')
    msg.add_alternative(html_body, subtype='html')

    files = ['Book1.xlsx',
             'Book2.xlsx',
             'stock-image.jpeg',
             'data.csv']
    for file in files:
        with open(file, 'rb') as f:
            ctype, encoding = mimetypes.guess_type(file)

            # If unable to guess
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'

            maintype, subtype = ctype.split('/', 1)
            msg.add_attachment(f.read(),
                               maintype=maintype,
                               subtype=subtype,
                               filename=file
                               )

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(from_email, password)
        smtp.send_message(msg)
        print('sent')


if __name__ == '__main__':
    send_mail()
