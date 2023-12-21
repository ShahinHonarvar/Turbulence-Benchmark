
import numpy as np

def submatrix_with_particular_sum(matrix):
    output = []
    row, col = matrix.shape
    for i in range(row):
        for j in range(col):
            for x in range(i,row):
                for y in range(j,col):
                    submatrix = matrix[i:x+1, j:y+1]
                    if np.sum(submatrix) == 34:
                        output.append(submatrix.tolist())
    return output
