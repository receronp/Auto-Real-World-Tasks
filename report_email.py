#!/usr/bin/env python3
import os
import sys
import reports
import emails
from datetime import date

def data_to_str(data):
    str_data = ""
    for item in data:
        str_data = str_data + "<br/>name: " + item["name"] + "<br/>weight: " + item["weight"] + "<br/>"
    return str_data


def main(argv):
    path = "supplier-data/descriptions/"
    files = os.listdir(path)
    desc = []
    for msg_file in files:
        fruit_desc = {}
        with open(os.path.join(path, msg_file)) as msg:
            fb = msg.readlines()
            fruit_desc["name"] = fb[0].strip()
            fruit_desc["weight"] = fb[1].strip()
        desc.append(fruit_desc)

    data_str = data_to_str(desc)
    reports.generate_report("/tmp/processed.pdf", "Processed Update on " + date.today().strftime("%B %d, %Y"),data_str)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)

if __name__ == "__main__":
    main(sys.argv)

