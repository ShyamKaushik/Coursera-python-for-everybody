fh = open("words.txt")
for line in fh:
    print(line.upper().rstrip())
    print(line.rstrip())