fname = input('Enter the file song_title ')
fhandle = open(fname)

line_word = list()
time = list()
hrs = int()
hrs_dict = dict()
for line in fhandle:
    if line.startswith('From '):
        line_word = line.split()
        time = line_word[5].split(':')
        hrs = time[0]
        hrs_dict[hrs] = hrs_dict.get(hrs,0) + 1

new_list = sorted(hrs_dict.items())

for k,v in new_list:
    print(k,v)
