#Autograder: 10.2
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
hours = dict()

for line in fh:
    if line.startswith('From '):
        line2 = line.split()    # Trough here, everything is familiar to you.
        h = line2[5].split(":") # Through here, everything becomes familiar to you. We choose the sixth element of the list 
                                # (which have index [5]), this is the time and it is divided where the ":" are (for example; "09:04:02").
        hours[h[0]] = hours.get(h[0], 0) + 1    # We are only interested in the hour, 
                                                #  fo that we take the first element of this list (list "h") that has an index [0] 
                                                # and push that data in the new list ("hours") and make the count.
 
lst = (sorted([(k,v) for k,v in hours.items()])) # Is necessary the two values, the key and the value (of the key) 
                                                 # to sort the data in proper order using the for loop.

for val, key in lst: # Once the data is sorted, it is printed, usin two values of the list again.
	print(val,key)

# A reason to not using tuples along this excersice is that Tuples are inmutables,