import requests
import json

url = "https://dog.ceo/api/breed/hound/images"

result = requests.get(url)
fields = json.loads(result.text)
print(list(fields))
lst1  = result.json().get("message")
k = 0
for i in range(len(lst1)):
    if  "hound-english" in str(lst1[i]):
        k += 1
    print(lst1[i])
print(len(result.json().get("message")))
print(result.text)
print(result)
print(k)

