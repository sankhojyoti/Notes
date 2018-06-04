import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt("example.txt", delimiter=",", unpack=True)

plt.plot(x, y, label="Loaded from file!")

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Graph 01\ncheck it out")
plt.legend()

plt.show()
