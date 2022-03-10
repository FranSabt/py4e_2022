def computepay(h, r): # Here the function is given a name and the arguments to be processed.
    #The indetetion below the definition of the function means that the code belong to the function.
    if hrs > 40:
        pay = (40 + (h - 40) * 1.5) * r
    else:
        pay = h * r
    return pay
    # For explanetion of the logic of the code see my Autograder:Exercise_3.1.py in chapter_04

hrs = int(input("Enter Hours:"))
rate = float(input("Enter rate:"))

p = computepay(hrs, rate) # Here We call the function a pass the data to operated.
                          # Be careful of the order of the date, if you pass first the rate an then the hours
                          # "hrs" will be assigned to "r" and "rate" to "h"

print("Pay", p)