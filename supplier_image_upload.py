#!/usr/bin/env python3
import os
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
path = os.path.dirname(os.path.abspath(__file__))
img_folder = "supplier-data/images"

for filename in os.listdir(os.path.join(path, img_folder)):
    if "jpeg" in filename:
        with open(os.path.join(os.path.join(path, img_folder), filename), 'rb') as opened:
            r = requests.post(url, files={'file': opened})

