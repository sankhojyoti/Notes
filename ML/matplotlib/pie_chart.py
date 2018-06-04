import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [2, 3, 6, 8, 13]

slices = [7, 2, 2, 13]
activities = ["sleeping", "eating", "working", "playing"]
colors = ["m", "c", "r", "b"]

plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, autopct="%1.1f%%")

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Graph 01\ncheck it out")
# plt.legend()

plt.show()
