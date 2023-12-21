
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    for x in range(rows):
        for y in range(cols):
            for i in range(x+1, rows+1):
                for j in range(y+1, cols+1):
                    submatrix = matrix[x:i, y:j]
                    if np.sum(submatrix) == -3:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
