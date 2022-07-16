import numpy as np
import matplotlib.pyplot as plt

#day one, the age and speed of 13 cars:
x1 = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y1 = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
#color = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
color = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80 , 90, 100])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x1, y1, c= color, cmap='winter', s= sizes, alpha= 0.5)


"""
#day two, the age and speed of 15 cars:
x2 = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y2 = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x2, y2, c= '#88c999')
"""
plt.colorbar()
plt.show()