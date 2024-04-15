import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipients, subject, message):
    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = ', '.join(recipients)
    email['Subject'] = subject

    email.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender_email, sender_password)

    server.sendmail(sender_email, recipients, email.as_string())

    server.quit()

sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
recipients = ['amanchauhan813@gmail.com', 'recipient2@example.com']
subject = 'Test Email'
message = 'This is a test email sent from Python.'

send_email(sender_email, sender_password, recipients, subject, message)
