from urllib.request import urlopen
import xml.etree.cElementTree as ET
url = 'http://py4e-data.dr-chuck.net/comments_961602.xml'

xml_tags = urlopen(url).read();
tree = ET.fromstring(xml_tags)

comm_list = tree.findall('comments/comment')
sum = 0
for item in comm_list:
    num = int(item.find('count').text)
    sum += num

print(sum)