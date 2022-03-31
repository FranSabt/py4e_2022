import re
number = 0
total = 0
value = 0
file = input("File: ")
fh = open(file)
print("file:",  fh)


for line in fh:
    line2 = line.strip()
    x = re.findall('\s*[0-9]+\s*', line2) # This regex will give us only estring of numbers
                                          # "s*" will macth from a white space troug number 
                                          # to another white space
    if x != []: # All the lines that not contains number will be emtpy dictionaries
                # so we wanted avoid these in order to obtein numbers.
        for number in x: # "x" contains dictionaries, even if they have only one number, 
                         #so we need to traverse every one of the elements of the dictionary.
            total += int(number)  # And finally, we transform the string to int a make the sum.
            value += 1 # Keep the count

print(total, "", value)

