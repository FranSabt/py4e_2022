# Trough here, nothing new, we ask the user for an input a 
# is parse the string to numerical data.
hrs = int(input("Enter Hours:"))
rate = float(input("Enter rate:"))


if hrs > 40: # Here is check is the hours have overtime.
    pay = (40 + (hrs - 40) * 1.5) * rate
    # If whe have overtime, whe know that the person have the 40 hours of normal work and don't need a variable 
    # to store that data.
    # What we need is the extra hours that is equeal to """hrs - 40(normal hours of work)""", 
    # and multiply the result for the over time. 
    # Finally is added to the 40 hrs and multiply by the normal rate.

else: #If no extra hours, the simple formula apllies.
    pay = hrs * rate 
    
print(pay)