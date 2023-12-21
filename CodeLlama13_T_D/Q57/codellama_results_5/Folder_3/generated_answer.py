
import numpy as np
def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    for i in range(n-1):
        for j in range(m-1):
            if np.sum(matrix[i:i+2,j:j+2]) == 54:
                return [matrix[i:i+2,j:j+2]]
    return []
