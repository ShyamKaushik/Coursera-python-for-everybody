from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://py4e-data.dr-chuck.net/comments_961600.html').read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
sum = 0
for span in soup.find_all('span'):
    s_span = str(span)

    num = re.findall('>([0-9]+)<',s_span)
    for n in num:
        sum = sum + int(n)

print(sum)