from re import X


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.issubset(y)

print(z)