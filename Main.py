from email_client import EmailClient

# Replace these with your actual email and server settings
SMTP_SERVER = 'smtp.gmail.com.com'
SMTP_PORT = 587
IMAP_SERVER = 'imap.gmail.com'
EMAIL_USER = 'cybersec.fso@gmail.com'
EMAIL_PASS = 'Fullsail1!'

# Create an instance of the EmailClient
client = EmailClient(SMTP_SERVER, SMTP_PORT, IMAP_SERVER, EMAIL_USER, EMAIL_PASS)

# Sending an email
client.send_email(
    to_address='julius.flow1@gmail.com',
    subject='Test Email',
    body='This is a test email sent from AnthonyF in Python.',
    attachments=['path/to/file.txt']
)

# Receiving emails
client.fetch_emails()