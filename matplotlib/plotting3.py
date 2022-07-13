import sys
import matplotlib
from matplotlib import markers

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

#plt.plot(ypoints, 'x-.r')
#plt.plot(ypoints, marker = 'o', ms = 20, mfc = '#4caf50', mec = 'r')
#plt.plot(ypoints, linestyle= 'dashed')
#plt.plot(ypoints, ls= '-.', color= 'r')
plt.plot(ypoints, c= 'hotpink', linewidth= 20.5)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()