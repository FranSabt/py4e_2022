#Autograder: 10.2
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
hours = dict()

for line in fh:
    if line.startswith('From '):
        line2 = line.split()
        h = line2[5].split(":")
        hours[h[0]] = hours.get(h[0], 0) + 1
 
lst = (sorted([(k,v) for k,v in hours.items()]))

for val, key in lst:
	print(val,key)