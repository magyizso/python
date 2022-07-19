fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
for x in "banana":
    print(x)
for x in range(2, 30, 3):
    if x == 11: break
    print(x)
else:
    print("Finally finished!")