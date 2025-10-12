import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL : ")
position = int(input("Position: "))
repeat = int(input("Repeat: "))

for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    tag = tags[position - 1]
    url = tag.get('href', None)

last = url.split("_")[2].split(".")[0]
print(last)
    
