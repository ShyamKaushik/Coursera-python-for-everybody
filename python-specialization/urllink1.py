from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'http://py4e-data.dr-chuck.net/known_by_Anureet.html'

for i in range(7):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    a_tags = soup('a')
    tag = a_tags[17]
    url = tag.get('href',None)

name = re.findall('_([A-Za-z]+)[.]',url)
print(name[0])
