#!/usr/bin/env python3

import requests
import sys
import time

def put(file):
    file = {'file':open(file, 'rb')}
    return requests.post("https://pyrubi.b80.xyz/upload.php",files=file).json()['result']

def box(msg):
    return "[{}] {}".format(time.strftime('%H:%M:%S'), msg)

lis = sys.argv

if "--path" in lis:
    path = lis[lis.index("--path")+1]
    
    print(box('Founded Path: {}'.format(path)))
    print(box('Start Uploading ...'))
    start = time.time()
    data = put(path)
    end = time.time()
    print(box('Link: {}'.format(data)))
    print(box(f'Process Ended in {end-start:.2f}'))
    
if "--help" in lis or "-h" in lis:
    print('python3 {} --path <PATH>\n               --path /storage/emulated/0/Download/test.txt'.format(lis[0]))

if len(lis) <= 1:
    print('python3 {} --path <PATH>\n               --path /storage/emulated/0/Download/test.txt'.format(lis[0]))
    
