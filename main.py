from astar3D import*
import numpy as np
import porespy as ps

start=(0,0,0)
end=(9,9,9)
maze=ps.generators.blobs(shape=[10, 10,10], porosity=0.5, blobiness=2)
maze=np.logical_not(np.array(maze,dtype=int))
maze=np.array(maze,dtype=int)

result=astar(maze,start,end)
print(result)