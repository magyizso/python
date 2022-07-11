from unittest import result


def my_func():
    print("Hello from a function.")

my_func()

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_func2(fname, lname):
    print(fname + " " + lname)

my_func2("Emil", "Refnes")

def my_func3(*kids):
    print(" The youngest kid is " + kids[2])

my_func3("Emil", "Tobias", "Linus")

def m_func4(child3, child2, child1):
    print('The youngest child is ' + child3)

m_func4(child1="Emil", child2="Tobias", child3="Linus")

def m_func(**kid):
    print("His lastname is " + kid["lname"])

m_func(fname = "Emil", lname = "Refnes")

def m_func2(country = "Norway"):
    print("I'm from " + country)
m_func2("Sweden")
m_func2("Brasil")
m_func2()
m_func2("India")

def m_func3(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

m_func3(fruits) 

def m_func5(x):
    return 5 * x

print(m_func5(3))
print(m_func5(5))
print(m_func5(9))

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(10)