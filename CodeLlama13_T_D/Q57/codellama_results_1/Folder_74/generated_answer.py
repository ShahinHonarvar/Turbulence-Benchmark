
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    for i in range(m-1):
        for j in range(n-1):
            submatrix = matrix[i:i+2, j:j+2]
            if np.all(submatrix == 88):
                return submatrix
    return []
