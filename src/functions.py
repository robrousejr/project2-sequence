# Creates zero filled matrix based on size of strains
def createMatrix(xSize, ySize):
    return [[0]*ySize for i in range(xSize)]