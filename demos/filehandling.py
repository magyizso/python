"""
f = open("demofile.txt", "r")

print(f.read(5))
print(f.readline())
print(f.readline())

for x in f:
    print(x)
f.close()

f = open("demofile2.txt", "a")
f.write("Now file has more content!")
f.close

f = open("demofile2.txt", "r")
print(f.read())
"""
f = open("demofile3.txt", "w")
f.write("Woops, I have deleted the content.")
f.close()

f = open("demofile3.txt", "r")
print(f.read())

import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist.")

