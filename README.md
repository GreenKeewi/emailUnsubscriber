# Email Unsubscriber Tool

A simple Python script to automatically extract unsubscribe links from your Gmail inbox. This tool connects to your email account, searches for emails containing "unsubscribe," and extracts the relevant links.

```EMAIL="your_email@gmail.com"
PASSWORD="your_app_password"```

## Important:
[]Password refers to a Google App Password, not your regular Gmail password.
[]If you haven't set up an App Password before, you'll need to enable 2-Factor Authentication (2FA) on your Google account.

2. Install Dependencies
Ensure you have the required Python packages installed:

pip install -r requirements.txt

3. Run the Script
Execute the script with:
```
python main.py
```
The script will connect to your Gmail inbox, search for emails containing "unsubscribe," and print the extracted links.

## Features:
[x] Secure IMAP connection to your Gmail inbox
[x] Extracts unsubscribe links from HTML email content
[x] Handles errors gracefully and skips problematic emails
