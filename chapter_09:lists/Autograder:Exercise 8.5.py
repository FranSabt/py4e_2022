count = 0

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
for line in fh:
    if line.startswith('From:'):
        count += 1
        for mail in line.split():
            if '@' in mail: 
                print(mail)


print("There were", count, "lines in the file with From as the first word")



"""
for line in fh :
    if line.startswith("From:") :
        count = count + 1
        lines = lines.split()
        print (lines[1])
"""