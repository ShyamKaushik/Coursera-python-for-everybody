fname = input('Enter the file song_title ')
fhandle = open(fname)

count = 0
word = list()
for line in fhandle:
    if line.startswith('From '):
        word = line.split()
        print(word[1])
        count += 1

print('There were',count,'lines in the file with',word[0],'as the first word')