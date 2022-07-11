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

thisdict["color"] = "red"
print(x)

thisdict.update({"made" : "USA"})
print(thisdict)

if "model" in thisdict:
    print("Yes, model exists in this dict.")