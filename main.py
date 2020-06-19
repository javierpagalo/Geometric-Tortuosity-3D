from astar3D import*
import numpy as np
from Tortuosity import *
import porespy as ps
from PorousMedium import *



"""
maze=ps.generators.blobs(shape=[10, 10,10], porosity=0.7, blobiness=0.5)
maze=np.logical_not(np.array(maze,dtype=int))
maze=np.array(maze,dtype=int)

result=findPoints(maze, "E")
print(maze.shape)"""




SIZE = 10
SHAPE = list(SIZE for _ in range(3))
for i in range(3):
    generate,maze=generate_blobs(SHAPE,0.60,0.5)
    maze=np.logical_not(np.array(maze,dtype=int))
    maze=np.array(maze,dtype=int)
    structure_processing(generate,"blobs"+str(i))
    result=geometric_tortuosity(maze)
    print(result)

