import numpy as np
from NetworkPorous import*


def matrixdivisor(matrix,slices): #Divide la matriz en una cantidad de slices, y bota una lista de arrays
    matrixes = []
    slicev = np.split(matrix,slices)
    for i in range(slices):
        slicey = np.hsplit(slicev[i],slices)
        matrixes.append(slicey)
    return matrixes

def listasinternas(liste): #Transforma la lista de arrays en una lista de listas
    lista=[]
    for elem in liste:
        listin = []
        for j in range(len(elem)):
            listin.append(list(map(list, elem[j])))
        lista.append(listin)
    return lista

def dict2DMatrix(array,suma): #[array] es la lista representativa de la matriz en 2 dimensiones,[suma] es la dimension de cada slice: suma = int(np.shape(medium)[0]/slices)

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
    return dic # Retorna el diccionario de las matriz cuyas primeras claves seran las columnas del array, y en cada una un diccionario con filas como claves.


#La propuesta es que el DFS en el momento de encontrar una coordenada en un medio dividido, le sume el valor de la columna y de la fila de acuerdo a sus claves
#print(medium)
#dic{fila={colum}}
count=0

     


"""----------------------------------------------------------"""
def maxPorous(resultado):
    newdata=[]
    comprobador=0
    for mazi  in resultado:
        newmaze=np.array(mazi)
        if (newmaze.sum()>comprobador):
            newdata=newmaze
            comprobador=newmaze.sum()
    return newdata
    

"""----------------------------------------------------------"""
def pointmedium(maze):
    centrodemasa=[]
    ROW,COL=len(maze),len(maze)
    for i in range(ROW):
        for j in range(COL) :
            if (maze[i][j]==1):
                centrodemasa.append((i,j))
    eligido=math.floor(len(centrodemasa)/2)
    return centrodemasa[eligido]


def endPoints(medium):
    slices = 10     # CORTES HORIZONTALES Y VERTICALES NXN=100 CORDES DE MATRIX 10X10
    suma = int(np.shape(medium)[0]/slices)
    arraymedium = matrixdivisor(medium,slices)
    listmedium = listasinternas(arraymedium)
    dicmedium = dict2DMatrix(listmedium,suma)
    end_points=[]
    for fila,columnas in dicmedium.items():
        print("="*10)
        for  k ,valor in columnas.items():
            ROW,COL=len(valor),len(valor)
          
            resultado=Graph(ROW,COL,valor).countPaths()
            print(resultado)
        
            #newresultado=convert_individual_paths(resultado)
            #print(newresultado)
            
           # mzi=maxPorous(resultado)
           # point=pointmedium(mzi)
            #end_points.append((fila + point[0],k + point[1],99))
        print("="*10)
    return end_points
    



"""TESTING"""




