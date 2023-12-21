
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    
    for i in range(n):
        for j in range(m):
            for k in range(i+1, n+1):
                for l in range(j+1, m+1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == 40:
                        result.append(submatrix.tolist())
    
    return result
