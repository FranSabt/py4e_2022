mail_c = dict()


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

    
fh = open(name)
for line in fh:
    if line.startswith('From:'):
        for mail in line.split():
            if '@' in mail: # Trough here nothing new. Remember that looks for the '@' if a safeguard against errors.
                mail_c[mail] =  mail_c.get(mail, 0) + 1 # This procedure allows getting the process in one line 
                                                        # of checking keys and counting their values.

max_k = max(mail_c, key = mail_c.get) # This function gets the string with a higher value key.
max_v = max(mail_c.values()) # The same but get the value of the key.
    
print(max_k, max_v)


"""
most_mail = ""
most_count = 0

for count in mail_c:
    if mail_c[count] > most_count:
        most_count = mail_c[count]
        most_mail = count
""" 
# This was my original solution, but I looked for a more pythonic way of making the same achievement.