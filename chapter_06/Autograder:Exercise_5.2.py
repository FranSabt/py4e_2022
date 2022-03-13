from cgitb import small


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    int(num)
    if num == 'done': break
    elif largest == None or num > largest: 
        largest = num
    elif smallest == None or num < smallest:
        smallest = num
    else: print('Invalid input')

print("Maximum", largest)
print('Minimun', smallest)