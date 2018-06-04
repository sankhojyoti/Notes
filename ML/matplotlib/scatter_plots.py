import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 7, 3, 8, 5, 7, 9, 2, 1]

plt.scatter(x, y, label="skitscat", color="k", s=200, marker="x")  # s is size

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Graph 01\ncheck it out")
# plt.legend()

plt.show()
