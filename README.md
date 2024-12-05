# Email Unsubscriber Tool 📧

A simple Python script to automatically extract unsubscribe links from your Gmail inbox. This tool connects to your email account, searches for emails containing "unsubscribe," and extracts the relevant links.

## Usage:
```
EMAIL="your_email@gmail.com"
PASSWORD="your_app_password"
```
## Important ❗:
1. Password refers to a Google App Password, not your regular Gmail password.
2. If you haven't set up an App Password before, you'll need to enable 2-Factor Authentication (2FA) on your Google account.

## 1. Install Dependencies
Ensure you have the required Python packages installed:
```
pip install -r requirements.txt
```
## 2. Run the Script
Execute the script with:
```
python main.py
```
The script will connect to your Gmail inbox, search for emails containing "unsubscribe," and print the extracted links.

## Features:
1. Secure IMAP connection to your Gmail inbox
2. Extracts unsubscribe links from HTML email content
3. Handles errors gracefully and skips problematic emails
