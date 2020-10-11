import re

fname = input('Enter file song_title ')
fhandle = open(fname)
content = fhandle.read()

snums = re.findall('[0-9]+',content)
sum = 0
for i in snums:
    num = int(i)
    sum += num

print(sum)