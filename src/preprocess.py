import os
import email
import pandas as pd

def parse_email_file(file_path):
    with open(file_path, 'r', errors='ignore') as f:
        msg = email.message_from_file(f)

    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body += str(part.get_payload())
    else:
        body = msg.get_payload()

    return {
        "sender": msg.get("From"),
        "receiver": msg.get("To"),
        "subject": msg.get("Subject"),
        "date": msg.get("Date"),
        "body": body
    }


# def load_emails(dataset_path):

#     emails = []

#     for root, dirs, files in os.walk(dataset_path):
#         for file in files:

#             file_path = os.path.join(root, file)

#             try:
#                 email_data = parse_email_file(file_path)
#                 emails.append(email_data)

#             except:
#                 continue

#     df = pd.DataFrame(emails)

#     return df

def load_emails(dataset_path, limit=500):

    emails = []

    for root, dirs, files in os.walk(dataset_path):

        for file in files:

            file_path = os.path.join(root, file)

            try:
                email_data = parse_email_file(file_path)
                emails.append(email_data)

                if len(emails) >= limit:
                    return pd.DataFrame(emails)

            except:
                continue

    return pd.DataFrame(emails)