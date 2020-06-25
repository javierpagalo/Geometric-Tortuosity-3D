import numpy as np

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

def Dict2DMatrix(array,suma): #[array] es la lista representativa de la matriz en 2 dimensiones,[suma] es la dimension de cada slice: suma = int(np.shape(medium)[0]/slices)

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

slices = 10
medium = np.random.randint(0,2,(100,100))
suma = int(np.shape(medium)[0]/slices)

arraymedium = matrixdivisor(medium,slices)
listmedium = listasinternas(arraymedium)
dicmedium = Dict2DMatrix(listmedium,suma)
#La propuesta es que el DFS en el momento de encontrar una coordenada en un medio dividido, le sume el valor de la columna y de la fila de acuerdo a sus claves
print(medium)
print(dicmedium)
print(np.array(dicmedium[0][0]))

#Prueba para coordenadas
tuplacoord =[]

for k,v in dicmedium.items():
    for u,w in v.items():
        tuplacoord.append((9+k,9+u))
print(tuplacoord)
