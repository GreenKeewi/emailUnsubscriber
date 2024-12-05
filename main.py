from dotenv import load_dotenv
import os
import imaplib
import email
from bs4 import BeautifulSoup

load_dotenv()

username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def connect_to_mail():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", timeout=30)  # Set a timeout
        mail.login(username, password)
        mail.select("inbox")
        return mail
    except imaplib.IMAP4.error as e:
        print(f"IMAP Connection Error: {e}")
        return None

def extract_links_from_html(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        links = [link["href"] for link in soup.find_all("a", href=True) if "unsubscribe" in link["href"].lower()]
        return links
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        return []

def searchForEmail():
    mail = connect_to_mail()
    if not mail:
        return []

    print("Searching for all emails containing 'unsubscribe'...")
    _, search_data = mail.search(None, '(BODY "unsubscribe")')  # Search all emails containing 'unsubscribe'
    email_ids = search_data[0].split()

    print(f"Found {len(email_ids)} emails to process.")
    links = []

    for num in email_ids:
        try:
            print(f"Processing email {num.decode()}")
            _, fetched_data = mail.fetch(num, "(RFC822)")
            raw_email = fetched_data[0][1]
            msg = email.message_from_bytes(raw_email)

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/html":
                        html_content = part.get_payload(decode=True).decode(errors='ignore')
                        links.extend(extract_links_from_html(html_content))
            else:
                if msg.get_content_type() == "text/html":
                    html_content = msg.get_payload(decode=True).decode(errors='ignore')
                    links.extend(extract_links_from_html(html_content))
        except Exception as e:
            print(f"Failed to process email {num.decode()}: {e}")
            continue

    mail.logout()
    return links

links = searchForEmail()
print(links)
