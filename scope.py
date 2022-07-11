x = 200

def myfunc():
    global x
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

print(x)