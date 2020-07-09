import numpy as np
import matplotlib.pyplot as plt


def path_format(path):

    pointers = np.array(path)

    x = pointers[:, 0]
    y = pointers[:, 1]
    z = pointers[:, 2]
    return x, y, z


def show_paths_on_porous_medium(paths):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    count = 0
    for data in paths:
        x, y, z = path_format(data)

        ax.plot(x, y, z, color="C"+str(count))
        count += 1
    plt.xlabel("X axis label")
    plt.ylabel("Y axis label")

    plt.show()
    """
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    for path in paths:
        ax.plot(path[0], path[1],path[2], color="red")
    plt.show()"""


paths = [[(1, 1, 1), (9, 1, 3), (7, 4, 2), (1, 2, 1), (3, 4, 5)], [
    (1, 1, 5), (9, 4, 3), (7, 5, 2), (1, 2, 1), (1, 4, 4)]]
# print(path_format(paths[0]))
# show_paths_on_porous_medium(paths)
