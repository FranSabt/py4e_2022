try:
    score = float(input("Enter Score: "))
    # Whit this code we parse the input in one statement, if it fail for any reason, 
    # like the user type a character instead of a number, the except is executed. 
except:
    print("Invalid input")
    quit()

if score < 0 or score > 1: # Here we check that the number is in the valid range.
    print("Invalid input")
    quit()
# Now, score is compare to the minimal range of every grade.
# If the socre is equeal or mayor to the minimal range, print the score.
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6: # Everything below this range is "F" grade.
    print("D")
else: 
    print("F")
