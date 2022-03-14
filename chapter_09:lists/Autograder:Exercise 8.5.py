count = 0

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
for line in fh:
    if line.startswith('From:'):
        for mail in line.split(): # I chose the name of the variable because it is what I looking for.
            if '@' in mail: # If the string/data contains an "@"  it will print the data and make the count.
                count += 1
                print(mail)


print("There were", count, "lines in the file with From as the first word")

# So, the code below is how most people resolve the exercises, but I think it's not the best solution, 
# is possible that for any reason the second data in the list is not the mail, in that case, your code will end up broken.
# But is a code that gets the desired result, it's up to you to decide.

"""
for line in fh :
    if line.startswith("From:") :
        count = count + 1
        lines = lines.split()
        print (lines[1])
"""
