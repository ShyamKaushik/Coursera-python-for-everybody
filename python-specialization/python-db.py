import _sqlite3

conn = _sqlite3.connect('countdb.sqlite')
curr = conn.cursor()

# curr.execute('''CREATE TABLE Counts (
#                 org TEXT,
#                 count INTEGER)''')

curr.execute('''DELETE from Counts''')
conn.commit()

fname = input('Enter the file song_title ')
fhandle = open(fname)

for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        email = words[1]

        curr.execute('SELECT count from Counts WHERE org = ?',(email,))
        count_ret = curr.fetchone()
        if count_ret is None:
            curr.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(email,))
        else:
            curr.execute('UPDATE Counts SET count = count+1 WHERE org = ?',(email,))

conn.commit()

str1 = 'SELECT org,count from Counts ORDER BY count DESC'

count = dict()
for row in curr.execute(str1):
    org_email = str(row[0])
    org_email_list = org_email.split('@')
    dom = org_email_list[1]

    if dom in count:
        count[dom] = count[dom] + row[1]
    else:
        count[dom] = row[1]

curr.execute('''DELETE from Counts''')

for k,v in count.items():
    curr.execute('INSERT into Counts (org,count) VALUES (?,?)',(k,v))

conn.commit()

for row in curr.execute(str1):
    print(row[1])
    break

conn.close()