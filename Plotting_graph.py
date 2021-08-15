import numpy as np
import matplotlib.pyplot as plt

x=np.array([10,20,30,40,50])

o=np.array([45,190,435,780,1125])
plt.style.use("seaborn")
plt.title("Comparison B/W Number of Inputs & Comparisons")

plt.plot(x,o,label="Bubble Sort")
plt.xlabel("Number of Inputs")
plt.ylabel("Number of Comparisons")
plt.legend()
plt.show()
