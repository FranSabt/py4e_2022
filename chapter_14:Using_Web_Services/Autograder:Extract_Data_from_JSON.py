import json
import urllib.request, urllib.parse, urllib.error
import ssl


lst = list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.json'


uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())

info = json.loads(data)
print('User count:', len(info))


for item in info['comments']:
    lst.append(int(item['count']))

print(sum(lst))

# So, the principles of parsing JSON files are almost the same that XML, but here is more simple.
# The major difference with the XML exercise was that we need to specify the branch of the tree that we need to iterate in order 
# to obtain the data: "info['comments']".
# Where info is the entire tree, and comments is the branch, and inside this branch,
# we are looking for the "counts" that contains the numbers.