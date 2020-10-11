from urllib.request import urlopen
import json

url = 'http://py4e-data.dr-chuck.net/comments_961603.json'
data = urlopen(url).read()

json_info = json.loads(data)
num = 0
sum = 0
for item in json_info['comments']:
    num = int(item['count'])
    sum += num

print(sum)