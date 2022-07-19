"""
thislist=list(("apple", "banana", "cherry", ))
if "apple" in thislist:
    print("Yes, 'apple' is in this list")
tropical= ["mango", "pineapple", "papaya"]
thistuple= ("kiwi", "orange")
thislist.extend(thistuple)
thislist.pop()
del thislist
thislist.clear()
print(thislist)
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])
i= 0
while i< len(thislist):
    print(thislist[i])
    i= i+1
[print(x) for x in thislist]
"""
fruits=["apple", "banana", "cherry", "kiwi", "mango"]
""""
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)

newlist=[x for x in fruits if 'a' not in x]
#newlist= [x for x in fruits]
print(newlist)

newlist = [x for x in range(10) if x < 5]
"""
#newlist = ["hello".upper() for x in fruits]
newlist = [x if x != "banna" else "orange" for x in fruits]
print(newlist)
