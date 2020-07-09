import numpy as np
from networkPorous import*
import math


# Divide la matriz en una cantidad de slices, y bota una lista de arrays
def matrixdivisor(matrix, slices):
    matrixes = []
    slicev = np.split(matrix, slices)
    for i in range(slices):
        slicey = np.hsplit(slicev[i], slices)
        matrixes.append(slicey)
    return matrixes


def listasinternas(liste):  # Transforma la lista de arrays en una lista de listas
    lista = []
    for elem in liste:
        listin = []
        for j in range(len(elem)):
            listin.append(list(map(list, elem[j])))
        lista.append(listin)
    return lista


# [array] es la lista representativa de la matriz en 2 dimensiones,[suma] es la dimension de cada slice: suma = int(np.shape(medium)[0]/slices)
def dict2DMatrix(array, suma):

    dic = {}
    i = 0
    for elem in array:
        dic[i] = {}
        i = i + suma
    u = 0
    for k, v in dic.items():
        columna = array[int(k / suma)]
        j = 0
        for elem in columna:
            v[j] = elem
            j = j + suma
        u = u + 1
    # Retorna el diccionario de las matriz cuyas primeras claves seran las columnas del array, y en cada una un diccionario con filas como claves.
    return dic


# La propuesta es que el DFS en el momento de encontrar una coordenada en un medio dividido, le sume el valor de la columna y de la fila de acuerdo a sus claves
# print(medium)
# dic{fila={colum}}
count = 0


def maxPorous(resultado):
    newdata = []
    comprobador = 0
    for mazi in resultado:
        newmaze = np.array(mazi)
        if (newmaze.sum() > comprobador):
            newdata = newmaze
            comprobador = newmaze.sum()
    return newdata





def pointmedium(maze):
    centrodemasa = []
    ROW, COL = len(maze), len(maze)
    for i in range(ROW):
        for j in range(COL):
            if (maze[i][j] == 1):
                centrodemasa.append((i, j))
    eligido = math.floor(len(centrodemasa)/2)
    return centrodemasa[eligido]



def endPoints(medium,data):
    
    slices = int((np.array(medium).shape[0])/10)
    print(slices)
     # CORTES HORIZONTALES Y VERTICALES NXN=100 CORDES DE MATRIX 10X10
    suma = int(np.shape(medium)[0]/slices)
    arraymedium = matrixdivisor(medium, slices)
    listmedium = listasinternas(arraymedium)
    dicmedium = dict2DMatrix(listmedium, suma)
    end_points = []
    for fila, columnas in dicmedium.items():
        if(data=='S'):
            PO=0
        if(data=='E'):
            PO=len(medium)-1
        for k, valor in columnas.items():
            point=(0,0)
            ROW, COL = len(valor), len(valor)
            resultado = Graph(ROW, COL, valor).countPaths()
            if(len(resultado)==0):
                 end_points.append((fila + 5, k + 5, PO))
            else:
                newresultado = convert_individual_paths(resultado)

                mzi = maxPorous(newresultado)
                
                point = pointmedium(mzi)
                
                end_points.append((fila + point[0], k + point[1], PO))
                


    return end_points
    




