import json

person = {"name": "Креатив Отсутствие",
          "age": 47,
          "hobbies": ["Волейбол", "Хоккей", "Телевизор"]
          }
print(person)
print(person["age"])
print(type(person))

json_text = json.dumps(person)

print(json_text)
print(type(json_text))