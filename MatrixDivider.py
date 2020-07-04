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

slices = 10     # CORTES HORIZONTALES Y VERTICALES NXN=100 CORDES DE MATRIX 10X10
medium = np.random.randint(0,2,(100,100))

suma = int(np.shape(medium)[0]/slices)

arraymedium = matrixdivisor(medium,slices)
listmedium = listasinternas(arraymedium)
dicmedium = dict2DMatrix(listmedium,suma)
#La propuesta es que el DFS en el momento de encontrar una coordenada en un medio dividido, le sume el valor de la columna y de la fila de acuerdo a sus claves
#print(medium)
#dic{fila={colum}}
count=0
"""
for fila,columnas in dicmedium.items():
    for  k ,valor in columnas.items():
            print((fila,k))
            count += 1"""
     
test=dicmedium[0][0]

"""----------------------------------------------------------"""
ROW,COL=len(test),len(test)
resultado=Graph(ROW,COL,test).countPaths()
resultado=convert_individual_paths(resultado)
print(len(resultado))


"""----------------------------------------------------------"""
newdata=[]
comprobador=0
for mazi  in resultado:
    newmaze=np.array(mazi)
    print(newmaze)
    newdata.append(newmaze)
    if (newmaze.sum()>comprobador):
        newdata=newmaze
        comprobador=newmaze.sum()
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

print(pointmedium(newdata))
"""----------------------------------------------------------"""
#print(count)
#print(np.array(dicmedium[0][0]))
"""
#Prueba para coordenadas
tuplacoord =[]

for k,v in dicmedium.items():
    for u,w in v.items():
        tuplacoord.append((9+k,9+u))
#print(len(tuplacoord))"""
