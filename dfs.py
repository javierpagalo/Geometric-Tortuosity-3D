"""TESTING"""
from NetworkPorous import *



maze=[[1,0,0,0],[1,1,0,1],[1,0,1,0],[1,0,0,1]]
ROW=len(maze)
COL=len(maze)
resultado=Graph(ROW,COL,maze).countPaths()
print(resultado)