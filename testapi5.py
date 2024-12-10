import requests
import json

url = "https://swapi.dev/api/people/4/"

result = requests.get(url)
print(result.text)
fields = json.loads(result.text)
print(list(fields))
print(result.json().get("name"))
flst = []
lst1  = result.json().get("films")
for i in range(len(lst1)):
    fresult = requests.get(lst1[i])
    print(fresult.json().get("characters"))
    lst2 = fresult.json().get("characters")
    for j in range(len(lst2)):
        print(lst2[j])
        chresult = requests.get(lst2[j])
        print(chresult.json().get("name"))
        if chresult.json().get("name") not in flst:
            flst.append(chresult.json().get("name"))
print(flst)





url = "https://swapi.dev/api/films/1/"
result = requests.get(url)
fields = json.loads(result.text)
print(result.text)
print(fields)


