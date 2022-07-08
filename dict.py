from copy import copy
from pyexpat import model


thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = thisdict.keys()
print(x)

thisdict["year"] = 2020
print(x)

thisdict.update({"made" : "USA"})
thisdict["color"] = "red"
print(thisdict)

if "model" in thisdict:
    print("Yes, model exists in this dict.")

mydict = thisdict.copy()
thisdict.popitem()
print(thisdict)

for y in thisdict.values():
    print(y)
for y in thisdict.keys():
    print(y)
for x, y in thisdict.items():
    print(x, y)
thisdict.clear()
print(thisdict)

print(mydict)