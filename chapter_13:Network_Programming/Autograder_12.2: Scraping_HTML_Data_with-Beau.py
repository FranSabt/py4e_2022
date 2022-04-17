# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
sum = 0

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') #http://py4e-data.dr-chuck.net/comments_42.html
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor span
span = soup('span') # We change the code for looking the 'span' tag in the html file, these contains
for num in span:    # the numbers to extract.
    # We extract the number, parse to INT because it is a string and when do the sum immediately.
    sum += int(num.contents[0])

print('Total:', sum) # An we need to print the result.