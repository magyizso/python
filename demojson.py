import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])

z = json.dumps(y)

print(y)

person = {
    "name" : "John",
    "age" : 30,
    "married" : True,
    "divorced" : False,
    "children" : ("Ann", "Billy"),
    "pets" : None,
    "cars" : [
        {"model": "BMW E230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(person, indent=4, sort_keys=True))