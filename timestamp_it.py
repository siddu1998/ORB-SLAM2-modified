import os
import re

from datetime import datetime

def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

directory='./rgb'
for filename in sorted_aphanumeric(os.listdir(directory)):
    now = datetime.now()
    if filename.endswith(".jpg"): 
         print(datetime.timestamp(now),('rgb/{}').format(filename))
     
