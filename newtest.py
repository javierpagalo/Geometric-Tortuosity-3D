import numpy as np
from NetworkPorous import*

from Tortuosity import*
import porespy as ps
from MatrixDivider import* 
im=ps.generators.blobs([100,100,100],0.80,0.5)
matrix=np.logical_not(np.array(im,dtype=int))
maze=np.array(matrix,dtype=int)
listEndPoints=endPoints(maze[-1])
