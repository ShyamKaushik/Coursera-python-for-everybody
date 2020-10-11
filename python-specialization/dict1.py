fname = input('Enter the file song_title ')
fhandle = open(fname)

count = dict()
email = str()
for line in fhandle:
    if line.startswith("From "):
        #print(line.rstrip())
        word = line.split()
        email = word[1]

        #count[email] = count.get(email,0) + 1

        if word[1] in count:
            count[word[1]] += 1
        else:
            count[word[1]] = 1

max_count = None
email = None
for k,v in count.items():
    if max_count is None or max_count < v:
        (email,max_count) = (k,v)
        #max_count = v

print(email, max_count)