import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_bulk_email(sender_email, sender_password, recipients, subject, body):
    # Set up the SMTP server for Outlook
    smtp_server = "smtp-mail.outlook.com"
    port = 587  # For starttls

    # Create a secure SSL context
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()

    try:
        # Login to the email account
        server.login(sender_email, sender_password)

        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["Subject"] = subject

        # Attach the body of the email
        message.attach(MIMEText(body, "plain"))

        # Send the email to all recipients
        for recipient in recipients:
            message["To"] = recipient
            server.send_message(message)
            print(f"Email sent to {recipient}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        server.quit()

# Example usage
if __name__ == "__main__":
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"  # Use an app-specific password for better security
    recipients = ["client1@example.com", "client2@example.com", "client3@example.com"]
    subject = "Important Update"
    body = """
    Dear valued client,

    This is an automated message to inform you about...

    Best regards,
    Your Company
    """

    send_bulk_email(sender_email, sender_password, recipients, subject, body)
