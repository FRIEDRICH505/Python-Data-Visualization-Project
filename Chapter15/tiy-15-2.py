import matplotlib.pyplot as plt
cube = [1, 3, 9, 18, 36]
input_values = [1, 2, 3, 4, 5]
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)
ax.plot(input_values, cube, linewidth=3)
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 1100, 0, 1100000])
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
plt.show()
