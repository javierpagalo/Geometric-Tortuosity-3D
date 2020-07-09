"""TESTING"""
from NetworkPorous import *
from PorousMedium import *


pading,maze=generate_blobs([10,10],0.5,0.5)

ROW=len(maze)
COL=len(maze)
resultado=Graph(ROW,COL,maze).countPaths()

