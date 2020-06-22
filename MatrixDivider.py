import numpy as np
"""
mat = np.random.randint(0,2,(10,10,10))
"""
def matrixdivisor(matrix,slices=10):
    matrixes = []
    sliceh = np.hsplit(matrix,slices)
    for i in range(slices):
        slicey = np.dsplit(sliceh[i],5)
        matrixes.append(slicey)
    return matrixes





matrix= np.random.randint(0,2,(4,4))
print(matrix)
def matrixSections(matrix, slices=2):
    sectionMatrix=np.hsplit(matrix,slices)
    return sectionMatrix
    
print(matrixSections(matrix)[0])

