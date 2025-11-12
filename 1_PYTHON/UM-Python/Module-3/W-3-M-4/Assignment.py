import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "https://py4e-data.dr-chuck.net/comments_2213464.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
sum = 0
for tag in tags:
    num = tag.contents[0]
    sum = sum + int(num)

print(sum)