# IMPORTANT!!! This code does not run well in Python3.8, I have a machine that I cannot configure for python 3.10, 
# but in other machine or online interpreter works well.

largest = None
smallest = None
while True: # This means that the loop will always run as log the 'done' statement is not reached
    try:
        if num == 'done': break # This line has the objective to terminated the loop. 
        num = int(num)
        if largest == None or num > largest: # The variables has values "None", so, for the first number is necessary to
            largest = num                    # assing some number, the next comparison will do the job.
        elif smallest == None or num < smallest:
            smallest = num
        else : continue
    except: 
        print('Invalid input') # This line will run when the input is the input is no 'done' or a number,
                               # also, if you put a float it will be comberted to int.

print("Maximum", largest)
print('Minimun', smallest)
