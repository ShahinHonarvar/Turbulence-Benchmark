
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            submatrix = matrix[row:row+3, col:col+3]
            if np.all(submatrix == -27):
                return [submatrix]
    return []
