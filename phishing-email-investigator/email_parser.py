from email import message_from_file
def parse_email(filepath):
    with open(filepath, "r") as f:
        msg = message_from_file(f)
        sender = msg["From"]
        subject = msg["Subject"]
        body = msg.get_payload()
        return {"sender": sender, "subject": subject, "body": body}
if __name__ == "__main__":
    result = parse_email("sample_phishing.eml")
    print(result)
    