import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def email():
    # Email configuration
    sender_email = "dev.test83299@gmail.com"
    receiver_email = "saad29@somaiya.edu"
    password = "jgglqnoraifuzyle"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Gmail SMTP port

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Email with threat report"

    # Add body to email
    body = "This email has pdf threat report attached"
    message.attach(MIMEText(body, "plain"))

    # Attach PDF file
    pdf_filename = "temp/report.pdf"
    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= report.pdf",
    )

    message.attach(part)

    # Establish a secure connection with the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        # Login to the SMTP server
        server.login(sender_email, password)
        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())

    print('Email sent')

