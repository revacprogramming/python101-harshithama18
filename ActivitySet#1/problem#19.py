from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/comments_42.html"
reqs = urlopen(url, context=ctx)
html = reqs.read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
# print(html.getcode())
# print(html.read())
# print(html)
# print(tags)
lst=list()
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    
    Contents= tag.contents[0]
    nums=int(Contents)
    lst.append(nums)
print(sum(lst))

# <br />
# <br></br>
#<name>chuck</name>