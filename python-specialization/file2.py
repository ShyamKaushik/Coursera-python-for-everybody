fname = input('Enter file song_title ')
fh = open(fname)
count = 0
space = int()
t_spam = 0
for line in fh:
    if 'X-DSPAM-Confidence:' in line:
        #print(line.rstrip())
        space = line.find(' ')
        spam = float(line[space+1:])
        t_spam = t_spam + spam
        count += 1

avg_spam = t_spam/count
print("Average spam confidence:",avg_spam)