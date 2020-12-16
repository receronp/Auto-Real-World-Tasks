#! /usr/bin/env python3
import os
import requests

path = "supplier-data/descriptions"

def main():
    files = os.listdir(path)
    for msg_file in files:
        client_fb  = {}
        with open(os.path.join(path, msg_file)) as msg:
            fb = msg.readlines()
            client_fb["name"] = fb[0].strip()
            client_fb["weight"] = fb[1].strip().split()[0]
            client_fb["description"] = fb[2].strip()
            client_fb["image_name"] = msg_file.replace("txt","jpeg")
        r = requests.post("http://35.222.124.164/fruits/", data=client_fb)
        print("Status Code: {} ; Text: {}".format(r.status_code,r.text))

if __name__ == "__main__":
    main()

