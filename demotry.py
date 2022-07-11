try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong!")
try:
    print("Hello")
except:
    print("Something went wrong.")
else:
    print("Nothing went wrong.")
finally:
    print("The 'try..except' block is finished")
"""
x = -1

if x < 0:
   raise Exception("Sorry, no numbers below zero.")
"""
y = "Hello"

if not type(y) is int:
    raise TypeError("Only integers are allowed.")