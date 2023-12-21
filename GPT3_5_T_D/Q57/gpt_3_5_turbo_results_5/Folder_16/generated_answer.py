
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix_sum = np.sum(matrix[i:k+1, j:l+1])
                    if submatrix_sum == -157:
                        result.append(matrix[i:k+1, j:l+1].tolist())
    
    return result
