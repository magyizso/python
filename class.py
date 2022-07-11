class MyClass:
    x = 5
print(MyClass)

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

p2 = Person("John", "Doe")
p2.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear,"!")

x = Student("Mike", "Olsen", 2019)
x.welcome()