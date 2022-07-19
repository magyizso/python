quantity = 3
itemno = 567
price = 45
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars"
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
tex = "His name is {1}. {1} is {0} years old."
print(tex.format(age, name))

my_order = "I have a {carname}, it is a {model}."
print(my_order.format(carname = "Ford", model = "Mustang"))
