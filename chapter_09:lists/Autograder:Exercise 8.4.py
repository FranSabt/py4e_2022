fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    x = (line.split())
    for word in x:
        if word not in lst:
            lst.append(word)
            
# You must be already familiarized with the code, if not, check the solution to the "Strings" chapter.
# The only that we need is to check if the word is already in the list, if not it will appear, is not necessary to make an "else: continue",
# because if the code doesn't execute the append statement it will continue to the next iteration.

# It could be that in older versions of Python were necessary to make a continued statement, but I don-t know.

lst.sort() # We need to put some order in the list.      
print(lst)
