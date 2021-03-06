from astar3D import*
import numpy as np
from Tortuosity import *
import porespy as ps
from PorousMedium import *
import shutil
import time

import time
from visualation import *




"""
maze=ps.generators.blobs(shape=[10, 10,10], porosity=0.7, blobiness=0.5)
maze=np.logical_not(np.array(maze,dtype=int))
maze=np.array(maze,dtype=int)

result=findPoints(maze, "E")
print(maze.shape)"""
 
"""SIZE" is the size that the porous medium will have, NUMBER_MEDIUM the media quantities 
They will be saved in the 3dmodels folder """
SIZE = 20
SHAPE = list(SIZE for _ in range(3))
NUMBER_MEDIUM=5
start=time.time()
tortuosity_test=[]
document=open("Tortu_porsity.txt","a")
porosity=0.60
for i in range(NUMBER_MEDIUM):
    startf=time.time()
    generate, maze = generate_blobs(SHAPE, porosity, 0.5)
    maze = np.logical_not(np.array(maze, dtype=int))
    maze = np.array(maze, dtype=int)
    #structure_processing(generate, "blobs"+str(i))
    result,graphs= geometric_tortuosity(maze)
    #print(result)
    tortuosity_test.append(result)
    
    #show_paths_on_porous_medium(graphs)

    #shutil.move("blobs"+str(i)+".stl", "3dmodels/blobs"+str(i)+".stl")
    endf=time.time()
    tiempof=endf-startf
    print(str(result) +"------"+str(tiempof))
end=time.time()
tiempo=end-start
print("El tiempo de ejecucion de "+str(NUMBER_MEDIUM)+":"+str(tiempo))
print(tortuosity_test)
document.write("Porosity:\n"+str(porosity)+"\n")
document.write("Shape:\n"+str(SIZE)+"\n")
document.write("Tortuosity:\n")
for elem in tortuosity_test:
    document.write(str(elem)+"\n")

document.close()

