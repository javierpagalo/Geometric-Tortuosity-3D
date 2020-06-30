import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def show_paths_on_porous_medium(paths):
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    for path in paths:
        print("f")
    datasets = [{"x":[1,2,3], "y":[1,4,9], "z":[0,0,0], "colour": "red"} for _ in range(6)]
    print(datasets)
    for dataset in datasets:
        ax.plot(dataset["x"], dataset["y"], dataset["z"], color=dataset["colour"])

    plt.show()

show_paths_on_porous_medium("D")