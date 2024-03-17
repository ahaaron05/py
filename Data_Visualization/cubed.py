import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

ax.set_title("Cubed Numbers", fontsize=17, c='Blue')
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Cubed Value", fontsize=12)
ax.tick_params(axis="both", labelsize=12)

ax.axis([0, 5500, 0, 100000000000])

plt.show()
#plt.savefig("plot.png")