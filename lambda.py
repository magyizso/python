x = lambda a: a + 10
print(x(5))

x = lambda a, b: a*b
print(x(5, 6))

x = lambda a, b, c: a+b+c
print(x(5, 6, 2))

def myfunc(n):
    return lambda a: n * a

myduble = myfunc(2)
mytriple = myfunc(3)

print(myduble(11))
print(mytriple(11))