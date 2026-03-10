# Email configuration
sender_email = "dev.test83299@gmail.com"  # Replace with your Gmail email address
sender_password = "jgglqnoraifuzyle"       # Replace with your Gmail password
receiver_email = "saad29@somaiya.edu"
subject = "Test Email"
body = "This is a test email sent from Python."
smtp_server = "smtp.gmail.com"
smtp_port = 587 

import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email, sender_password)
# message to be sent
message = "Message_you_need_to_send second time"
# sending the mail
s.sendmail(sender_email, receiver_email, message)
# terminating the session
s.quit()