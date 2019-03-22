import os
import requests
import sys

KEY = os.environ.get('ACCESS_KEY')
IP = sys.argv[1] if len(sys.argv) == 2 else None

if not KEY:
    print('AccessKey Not Found.!')
    sys.exit(1)

if not IP:
    print('Please Provide IpAddress.!')
    sys.exit(1)

url =  "http://api.ipstack.com/{}?access_key={}".format(IP,KEY)
reply = requests.get(url)
code = reply.json()['country_code']
print('{} : {}'.format(IP,code))
