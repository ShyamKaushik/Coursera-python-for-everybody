fname = input('Enter the file song_title ')
fhandle = open(fname)

words = list()
f_list = list()
for line in fhandle:
    words = line.split()
    for word in words:
        if not word in f_list:
            f_list.append(word)
f_list.sort()
print(f_list)