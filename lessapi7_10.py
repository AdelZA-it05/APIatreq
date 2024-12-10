import requests

"""Создаём файл для списка персонажей"""
with open('charactlist.txt', 'w') as charactlist:
    pass
"""Актёр для поиска"""
url = "https://swapi.dev/api/people/4/"
result = requests.get(url)
print(result.json().get("name"))
"""Итоговый список персонажей"""
flst = []
"""Список фильмов с Darth Vader"""
lst1 = result.json().get("films")
for i in range(len(lst1)):
    fresult = requests.get(lst1[i])
    print('film: ' + fresult.json().get("title"))
    lst2 = fresult.json().get("characters")
    """Список персонажей из фильма """
    for j in range(len(lst2)):
        chresult = requests.get(lst2[j])
        """Проверка на дубли"""
        if chresult.json().get("name") not in flst:
            flst.append(chresult.json().get("name"))
            """Добавление в файл без дублей"""
            with open('charactlist.txt', 'a', encoding='utf-8') as charactlist:
                charactlist.write(chresult.json().get("name") + '\n')







