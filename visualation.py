import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def path_format(paths):
    pathFormat=[]
    for path in paths:
        pointers=np.array(path)
        pathFormat.append((pointers[:,0],pointers[:,1],pointers[:,2]))
    return pathFormat
    
        
def show_paths_on_porous_medium(paths):
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    for path in paths:
        ax.plot(path[0], path[1],path[2], color="red")
    plt.show()

    