import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Nikoleta.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print(url)
# Retrieve all of the anchor tags
tags = soup('a')
#for tag in tags:

  #print(tag.get('href', None))

#link = tag
for x in range(7):
 # tag = tags[2]
  tag = tags[17]
  link = tag.get('href',None)
  print(link)
  html2=urllib.request.urlopen(link, context=ctx).read()
  soup2 = BeautifulSoup(html2, 'html.parser')
  tags= soup2('a')

words=link.split('_')
word=words[-1].split('.')
print(word[0])