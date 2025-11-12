import xml.etree.ElementTree as ET
import urllib.request

url = input("Enter the URL :: ")
fhand = urllib.request.urlopen(url)
data = fhand.read()

tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum = 0
for num in counts:
    val = int(num.text)
    sum = sum + val
print(sum)
