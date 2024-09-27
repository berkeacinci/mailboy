# Mailboy

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

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/mailboy.git
   cd mailboy
   ```

2. Create a virtual environment:

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

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

This will install all necessary packages listed in the `requirements.txt` file.

## Configuration

1. In the project root directory, create a `config.json` file with the following structure:
   ```json
   {
     "sender_email": "your_email@outlook.com",
     "sender_password": "your_password",
     "smtp_server": "smtp-mail.outlook.com",
     "smtp_port": 587,
     "recipients": [
       "client1@example.com",
       "client2@example.com",
       "client3@example.com"
     ]
   }
   ```

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
- `--dry-run`: Perform a dry run without sending actual emails

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
   python mailboy.py --dry-run
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

## Troubleshooting

- If you encounter SMTP authentication errors, make sure your email provider allows less secure apps or generate an app-specific password.
- For Outlook users, you may need to enable IMAP in your account settings.

## Caution

- Be careful with the frequency and volume of emails you send to avoid being flagged as spam.
- Ensure you have permission to email the recipients in your list.
- Keep your `config.json` file secure, as it contains sensitive information.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/mailboy/issues) if you want to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.