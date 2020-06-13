




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
                list_points.append((0, i, j))
            if((maze[i][j] == 0) and position == "E"):
                list_points.append((final, i, j))
    return list_points

def geometric_tortuosity(maze):
    """
    The geometric tortuosity of a porous medium returns
    :param maze:
    :return geometric tortuosity:
    """
    path_star_list = findPoints(maze,"S")
    path_end_list = findPoints(maze,"E")

    total_caminos = []
    total_paths = len(path_end(maze))*len(path_star(maze))
    unit_caminos = 0
    array_path = np.array(maze)
    line = (array_path.shape)[2]
    for star in path_star_list:
        caminos = []
        for end in path_end_list:

            path = astar(maze, star, end)
            result = 0
            for i in range(len(path)-1):
                add = math.sqrt((path[i][0]-path[i+1][0])
                                ** 2 + (path[i][1]-path[i+1][1])**2+  (path[i][2]-path[i+1][2])**2)
                result += add
            caminos.append(result)
            unit_caminos += 1

        total_caminos.append(min(caminos))

    valor = (np.mean(np.array(total_caminos)))
    geometric_tortusity = valor/(int(line)-1)
    return geometric_tortusity
    