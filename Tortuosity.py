import numpy as np
from astar3D import*
import math
import random


def findPoints(medium, position):
    list_points = []
    if(position == "S"):
        maze = medium[0]
    else:
        final = len(medium)-1
        maze = medium[final]
    ROW = len(maze)
    COL = len(maze[0])
    for i in range(ROW):
        for j in range(COL):
            if((maze[i][j] == 0) and position == "S"):
                list_points.append((i, j, 0))
            if((maze[i][j] == 0) and position == "E"):
                list_points.append((i, j, final))
    return list_points


def valuepath(tupla):
    i = path.index(tupla)
    if i == len(path) - 1:
        return 0
    add = math.sqrt((path[i][0] - path[i + 1][0]) ** 2 + (path[i][1] - path[i + 1][1]) ** 2 + (
        path[i][2] - path[i + 1][2]) ** 2)
    return add


def geometric_tortuosity(maze):
    """
    The geometric tortuosity of a porous medium returns
    :param maze:
    :return geometric tortuosity:
    """
    path_star_list = findPoints(maze, "S")
    path_end_list = findPoints(maze, "E")

    total_caminos = []
    total_paths = len(path_end_list)*len(path_star_list)
    unit_caminos = 0
    array_path = np.array(maze)
    line = (array_path.shape)[2]
    global path
    i=0
    for star in path_star_list:
        caminos = []
        
        
        end=random.choice(path_end_list)
        path = astar(maze, star, end)
        print(i)
        i+=1
        result = 0
        # caminos.append(path)
        # total_caminos.append(caminos)
        try:
            x = map(valuepath, path)
            result = sum(x)
        except:
            pass

        caminos.append(result)
        unit_caminos += 1

        total_caminos.append(np.mean(caminos))

    valor = (np.mean(np.array(total_caminos)))
    geometric_tortusity = valor/(int(line)-1)
    return geometric_tortusity
