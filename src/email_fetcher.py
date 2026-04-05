import os
import imaplib
import email
from email.header import decode_header
import logging

logger = logging.getLogger(__name__)

def connect_imap():
    host = os.getenv("EMAIL_HOST")
    user = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    if not all([host, user, password]) or 'your_email' in user:
        logger.warning("Email credentials missing or default in config. Skipping email fetch.")
        return None
    
    try:
        mail = imaplib.IMAP4_SSL(host, port=int(os.getenv("EMAIL_PORT", 993)))
        mail.login(user, password)
        return mail
    except Exception as e:
        logger.error(f"Failed to connect to IMAP: {e}")
        return None

def fetch_email_data():
    """Checks emails and returns basic data parsed into a list of dicts."""
    mail = connect_imap()
    if not mail:
        return []
        
    folder = os.getenv("EMAIL_FOLDER", "INBOX")
    mail.select(folder)
    
    subject_search = os.getenv("EMAIL_SEARCH_SUBJECT", "")
    search_criteria = f'(SUBJECT "{subject_search}")' if subject_search else 'ALL'
    
    status, messages = mail.search(None, search_criteria)
    
    data_list = []
    if status == "OK" and messages[0]:
        # limit to last 5 messages for safety/brevity
        msg_nums = messages[0].split()[-5:]
        for num in msg_nums:
            res, msg_data = mail.fetch(num, '(RFC822)')
            if res != "OK":
                continue
                
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else 'utf-8')
                    sender = msg.get("From")
                    
                    data_list.append({
                        "Source": "Email",
                        "Subject": subject,
                        "Sender": sender,
                    })
                    
    mail.close()
    mail.logout()
    logger.info(f"Fetched {len(data_list)} emails matching criteria.")
    return data_list
