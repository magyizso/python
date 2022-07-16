from turtle import color, left
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

plt.title("Sports watch data", fontdict= font1, loc= 'left')
plt.xlabel("Average pulse", fontdict= font2)
plt.ylabel("Calorie burnage", fontdict=font2)

plt.grid(color= 'green', linestyle= '--', linewidth= 0.5)
#plt.grid(axis= 'y')
plt.show()