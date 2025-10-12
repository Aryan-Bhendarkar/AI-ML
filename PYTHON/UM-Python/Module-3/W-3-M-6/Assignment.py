import json
import urllib.request

url = input("Enter URL :: ")
fhand = urllib.request.urlopen(url)
data = fhand.read()

info = json.loads(data)
comments = info["comments"]
sum = 0
for comment in comments:
    num = int(comment["count"])
    sum = sum + num
print(sum)