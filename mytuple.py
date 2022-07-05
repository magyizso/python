from contextlib import redirect_stdout
import this


thistuple= ("apple", "banana", "cherry", "strawberry", "raspberry")
#print(thistuple[-4:-1])
#if "apple" in thistuple:
 #   print("Yes, thistuple has 'apple' in it.")
"""
y= list(thistuple)
y.remove("apple")
thistuple= tuple(y)

#del thistuple

(green, *tropic, red) = thistuple

print(green)
print(tropic)
print(red)

for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i])
"""
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1