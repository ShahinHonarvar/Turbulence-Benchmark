
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    for i in range(n-1):
        for j in range(m-1):
            for k in range(i+1, n+1):
                for l in range(j+1, m+1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -25:
                        return list(np.nditer(submatrix))
    return []
