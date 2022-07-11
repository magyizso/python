child1 = {
    "name" : "Tobias",
    "year" : 2004
}    
child2 = {
    "name" : "Emil",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
for x, y in myfamily.items():
    print(x, y)