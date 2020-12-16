#!/usr/bin/env python3
import os
import emails
import psutil
import socket

def check_cpu():
    return psutil.cpu_percent(1)

def check_disk():
    usage = psutil.disk_usage("/")
    if usage.percent < 20:
        return True
    return False

def check_mem():
    mem = psutil.virtual_memory()
    if mem.available * 1E-6 < 500:
        return True
    return False

def check_host():
    localhost = socket.gethostbyname('localhost')
    if localhost != "127.0.0.1":
        return True
    return False

def main():
    cpu = check_cpu()
    disk_space = check_disk()
    mem = check_mem()
    host = check_host()
    if cpu or disk_space or mem or host:
        if cpu:
            subject = "Error - CPU usage is over 80%"
        elif disk_space:
            subject = "Error - Available disk space is less than 20%"
        elif mem:
            subject = "Error - Available memory is less than 500MB"
        elif host:
            subject = "Error - localhost cannot be resolved to 127.0.0.1"

        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        body = "Please check your system and resolve the issue as soon as possible."
        message = emails.generate_email_report(sender, receiver, subject, body)
        emails.send_email(message)


if __name__ == "__main__":
    main()
