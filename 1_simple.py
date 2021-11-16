import smtplib
from config import from_email, password, to


def main():
    subject = "test subject 3"
    body = "sending mail from python is easy!"
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(from_email,
                   password)
        # Body Only
        # smtp.sendmail(from_email, to, body)
        # Subject and Body
        subject_and_message = f"Subject:{subject}\n{body}"
        smtp.sendmail(from_email, to, subject_and_message)

        print("sent")


if __name__ == '__main__':
    main()
