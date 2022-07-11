a = 330
b = 33
c = 500
#if a < b: print("b is greater than a")
print("A") if a > b else print("=") if a == b else print("B")
if a > b and c > b:
    print("both statement are true")
if a > b or a > c:
    print("At least on of condition is true.")

x = 41
if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above 20!")
    else:
        print("and not above 20.")