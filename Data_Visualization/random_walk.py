import random
import matplotlib.pyplot as plt

class RandomWalk:
    """Class to generate random walks"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Caluclate all the points in the walk"""

        while len(self.x_values) < self.num_points:
            x_direction = random.choice([1, -1])
            x_distance = random.choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = random.choice([-1, 1])
            y_distance = random.choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


rw = RandomWalk(152000)
rw.fill_walk()

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap= plt.cm.Blues, s=0.005)

ax.set_title("RANDOM WALK", fontsize=15, c='lavender')
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Cubed Value", fontsize=12)
ax.tick_params(axis="both", labelsize=12)

plt.show()