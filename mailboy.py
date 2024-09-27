import smtplib
import json
import argparse
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from tqdm import tqdm
import time

def load_config(file_path):
    with open(file_path, 'r') as config_file:
        return json.load(config_file)

def load_email_content(file_path):
    with open(file_path, 'r') as content_file:
        lines = content_file.readlines()
        subject = lines[0].strip().replace('Subject: ', '')
        body = ''.join(lines[2:])  # Skip the blank line after subject
    return subject, body

def personalize_email(body, recipient):
    # Simple personalization example
    return body.replace('{name}', recipient.split('@')[0])

def send_bulk_email(config, subject, body, dry_run=False):
    # Set up logging
    logging.basicConfig(filename='email_log.txt', level=logging.INFO,
                        format='%(asctime)s - %(message)s')

    # Set up the SMTP server
    server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
    server.starttls()

    try:
        # Login to the email account
        server.login(config['sender_email'], config['sender_password'])

        # Send the email to all recipients
        for recipient in tqdm(config['recipients'], desc="Sending emails"):
            try:
                message = MIMEMultipart()
                message["From"] = config['sender_email']
                message["To"] = recipient
                message["Subject"] = subject
                
                # Personalize the body
                personalized_body = personalize_email(body, recipient)
                message.attach(MIMEText(personalized_body, "plain"))

                if not dry_run:
                    server.send_message(message)
                    logging.info(f"Email sent to {recipient}")
                else:
                    print(f"Would send email to {recipient}")
                
                time.sleep(1)  # Add a small delay to avoid overwhelming the server
            except Exception as e:
                logging.error(f"Failed to send email to {recipient}: {str(e)}")
                print(f"Error sending to {recipient}: {str(e)}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")

    finally:
        server.quit()

def main():
    parser = argparse.ArgumentParser(description="Send bulk emails")
    parser.add_argument("--config", default="config.json", help="Path to config file")
    parser.add_argument("--template", default="email_content.txt", help="Path to email template file")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without sending emails")
    args = parser.parse_args()

    config = load_config(args.config)
    subject, body = load_email_content(args.template)
    send_bulk_email(config, subject, body, args.dry_run)

if __name__ == "__main__":
    main()
