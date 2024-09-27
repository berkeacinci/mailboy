import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_config(file_path):
    with open(file_path, 'r') as config_file:
        return json.load(config_file)

def send_bulk_email(config, subject, body):
    # Set up the SMTP server
    server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
    server.starttls()

    try:
        # Login to the email account
        server.login(config['sender_email'], config['sender_password'])

        # Create the email message
        message = MIMEMultipart()
        message["From"] = config['sender_email']
        message["Subject"] = subject

        # Attach the body of the email
        message.attach(MIMEText(body, "plain"))

        # Send the email to all recipients
        for recipient in config['recipients']:
            message["To"] = recipient
            server.send_message(message)
            print(f"Email sent to {recipient}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        server.quit()

# Example usage
if __name__ == "__main__":
    config = load_config('config.json')
    
    subject = "Important Update"
    body = """
    Dear valued client,

    This is an automated message to inform you about...

    Best regards,
    Your Company
    """

    send_bulk_email(config, subject, body)
