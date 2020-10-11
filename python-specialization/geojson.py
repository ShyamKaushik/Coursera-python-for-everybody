import urllib.request
import urllib.parse
import urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/json?'
location = input('Enter location: ')
key = 42
if len(location) < 1:
    exit(0)

url = url + urllib.parse.urlencode({'key':key}) + '&'
url = url + urllib.parse.urlencode({'address':location})

print('Retrieving',url)
data = urllib.request.urlopen(url).read().decode()

json_info = json.loads(data)
print('Retrived',len(data),'characters')
print(json_info['results'][0]['place_id'])