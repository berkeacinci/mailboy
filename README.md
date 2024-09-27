# Mailboy

**IMPORTANT: Please read this entire README file before using Mailboy. It contains crucial information for setup and usage.**

Mailboy is an automated email sender that allows you to easily send bulk emails to multiple recipients. It's designed to be flexible, user-friendly, and efficient for sending newsletters, updates, or any other type of mass communication.

## Features

- Send emails to multiple recipients simultaneously
- Use customizable email templates
- Personalize emails for each recipient
- Perform dry runs to test without sending actual emails
- Logging for tracking successful sends and errors
- Progress bar to visualize email sending progress

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. Create a folder named 'bots' (or any name you prefer) on your computer and open it in your code editor (e.g., VS Code, PyCharm, Cursor).

2. Open terminal and clone this repository by running the following commands:
   ```
   git clone https://github.com/berkeacinci/mailboy.git
   cd mailboy
   ```
   # Note: You might need to log in to your GitHub account first.

3. Create a virtual environment (venv) and activate it:

   - On Windows:
     ```
     python -m venv venv 
     venv\Scripts\activate
     ```

   - On macOS and Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
   # A virtual environment helps isolate your project dependencies from other Python projects.

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
   # This command installs all necessary packages listed in the `requirements.txt` file.

## Configuration

1. In the project root directory, create a `config.json` file with the following structure:
   ```json
   {
     "sender_email": "your_email@example.com",
     "sender_password": "your_password_or_app_password",
     "smtp_server": "smtp.example.com",
     "smtp_port": 587, 
     "recipients": [
       "client1@example.com",
       "client2@example.com",
       "client3@example.com"
     ]
   }
   ```
   
   # Important notes for beginners:
   # - "sender_email": Your email address that you'll use to send emails
   # - "sender_password": For Gmail and Outlook, you'll need to use an app password
   # - "smtp_server": Use "smtp.gmail.com" for Gmail, "smtp-mail.outlook.com" for Outlook
   # - "smtp_port": 587 is a common port for TLS encryption
   # - "recipients": List of email addresses you want to send to
   
   **Important:** Keep your `config.json` file secure and never commit it to version control, as it contains sensitive information.

2. Email Content:
   - A sample `email_content.txt` file is provided in the repository.
   - You can modify this file directly for your specific needs.
   - To create a new template, copy `email_content.txt` and rename it (e.g., `newsletter_template.txt`).

   The structure of the email content file should be:
   ```
   Subject: Your Email Subject Here

   Dear {name},

   Your email body goes here...

   Best regards,
   Your Name
   ```
   # The {name} placeholder will be replaced with the recipient's name.
## File Structure

Your project directory should look like this:

```
mailboy/
│
├── venv/                  # Virtual environment (created during installation)
├── mailboy.py             # Main script
├── config.json            # Configuration file (you need to create this)
├── email_content.txt      # Sample email template (provided)
├── requirements.txt       # List of Python dependencies
└── README.md              # This file
```

## Usage

Ensure your virtual environment is activated before running the script.

Run the script using the following command:

```
python mailboy.py [options]
```

### Options:

- `--config`: Specify a custom config file (default: `config.json`)
- `--template`: Specify a custom email template file (default: `email_content.txt`)
- `--dry-run`: Perform a dry run without sending actual emails. This is useful for testing your configuration and email content without actually sending emails.
### Examples:

1. Send emails using default config and template:
   ```
   python mailboy.py
   ```

2. Use a custom config and template:
   ```
   python mailboy.py --config newsletter_config.json --template monthly_update.txt
   ```

3. Perform a dry run:
   ```
   python mailboy.py --dry-run or python mailboy.py --dry-run --config config.json --template monthly_update.txt   
   ```

### Working with Email Templates

1. For quick use, modify the provided `email_content.txt` file with your specific content.

2. For different types of emails, create new template files:
   ```
   cp email_content.txt newsletter_template.txt
   ```
   Then edit `newsletter_template.txt` with your newsletter content.

3. To use a specific template:
   ```
   python mailboy.py --template newsletter_template.txt
   ```

## Personalization

You can personalize your emails by using `{name}` in your email template. This will be replaced with the recipient's name (derived from their email address).

## Logging

All email sending activities are logged in `email_log.txt` in the project directory.

## SMTP Services

If you're having trouble with your email provider's SMTP server, you might consider using a third-party SMTP service. These services often provide better deliverability and are designed for bulk sending. Some options include:

- SMTP2GO
- SendinBlue
- Mailgun

To use these services, you'll need to sign up for an account and update your `config.json` file with the provided SMTP server details.

## Troubleshooting

- If you encounter SMTP authentication errors, you may need to use an app-specific password or enable two-factor authentication for your email account.
- For Microsoft accounts (Outlook, Hotmail, Live, etc.), you might need to use an app password or switch to a different SMTP service as Microsoft has disabled basic authentication for many accounts.
- If you're using a work or school account, contact your IT administrator as they may need to enable SMTP AUTH for your organization.

## Caution

- Be careful with the frequency and volume of emails you send to avoid being flagged as spam.
- Ensure you have permission to email the recipients in your list.
- Keep your `config.json` file secure, as it contains sensitive information.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/mailboy/issues) if you want to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.