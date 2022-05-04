import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

sum = 0

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

'''
// This can be confusing, but the model give by the PY4E course has a few thng that 
we don't need, this because the page don't use a API-Key, and try to acces to the page using
a key give you errors.

api_key = False

if api_key is False:  
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
'''


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

# Trough here anithing new



'''
// Like above, this chunck of code is intendeed if you need a API-Key to acces to the page,
maybe is posible to use the code, but it more simple to ignore to codea continue.

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
'''

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())

tree = ET.fromstring(data)
counts = tree.findall('.//count')
# Whit this code "tree.findall('.//count')" we acces to the count inmediatly
# The two "/" indicate the level to look in the XML file.

lst = list()

for num in counts:
    lst.append(int(num.text))
    sum += int(num)

#print(sum(lst)) - I dint' make this line works :C

for num in lst:
    sum += num

print(sum)

