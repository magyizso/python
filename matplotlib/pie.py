from turtle import title
import numpy as np
import matplotlib.pyplot as plt

y = np.array([35, 25, 25, 15])
mylabel = ['Apples', 'Bananas', 'Cherries', 'Dates']
myexplode = [0.2, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4caf50"]


plt.pie(y, labels= mylabel, colors= mycolors , startangle= 90, explode= myexplode, shadow= True)
plt.legend(title= "Four fruits")
plt.show()