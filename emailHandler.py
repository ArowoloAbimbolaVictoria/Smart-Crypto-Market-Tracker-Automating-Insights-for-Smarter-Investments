import smtplib
import ssl
from email.message import EmailMessage
import os

EMAIL_SENDER = "sender_email_address"
EMAIL_PASSWORD = "sender_password"

def send_email(receiver_email, receiver_name, attachments=None):
    """
    Sends an email with multiple attachments.
    
    :param receiver_email: Email address of the recipient.
    :param receiver_name: Name of the recipient.
    :param attachments: List of file paths for attachments (optional).
    """
    msg = EmailMessage()
    msg["Subject"] = "📊 Crypto Market Update"
    msg["From"] = EMAIL_SENDER
    msg["To"] = receiver_email
    msg.set_content(
    f"Hello {receiver_name},\n\nToday's Crypto Trends Are In!\n\n"
    "Get the latest insights on the market’s top gainers and losers with a quick snapshot of today’s trends.\n\n"
    "Attached is your visual report to help you stay ahead of the market.\n\n"
    "Best,\nAbimbola Arowolo"
)
    # Attach multiple files
    if attachments:
        for attachment in attachments:
            if os.path.exists(attachment):
                with open(attachment, "rb") as f:
                    img_data = f.read()
                    msg.add_attachment(img_data, maintype="image", subtype="png", filename=os.path.basename(attachment))

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"✅ Email sent successfully to {receiver_email}!")
    except Exception as e:
        print(f"❌ Failed to send email to {receiver_email}: {e}")

def send_bulk_emails(personnel_list, attachments=None):
    """
    Sends emails to all recipients in the personnel list with multiple attachments.
    
    :param personnel_list: List of dictionaries containing names and email addresses.
    :param attachments: List of file paths for attachments.
    """
    for person in personnel_list:
        send_email(person["Email"], person["Name"], attachments)
