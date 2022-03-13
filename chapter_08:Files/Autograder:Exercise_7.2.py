# Use the file name mbox-short.txt as the file name

total = 0 # Total sum of confidence data
count = 0 # Total number of times that confidence appears
aver = 0  # Average 

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        total += (float(line[line.find(":")+1:]))
        count += 1
# The loop will check for the string "X-DSPAM-Confidence:", if exist, the second line extracts the floating-point number
# and the "+=" operator make a continuous sum. Count check for the number of times that the confidence appears.

aver = total / count
# And this is a basic formula to calculate a average point.

print("Average spam confidence:", aver)