# This first line is provided for you

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))
# Remember when we use "input" the data stored is not a number, is a string of f numbers characters
# In the same line we parse the string to float values.

print("Pay:", pay)

# Also you may try something like this: float(hrs * rate), but this doesn't work because
# it will try to make a multiplication first (that will fail), and then make the conversion 

 

# Finally, a silly thing, if you only print "pay" the webpage will tell you
# that you fail, is because the page evaluate the result exactly has is show to you.
# But think that a user will be confuse if you don't indicate precisely what 
# kind of information are you showing.