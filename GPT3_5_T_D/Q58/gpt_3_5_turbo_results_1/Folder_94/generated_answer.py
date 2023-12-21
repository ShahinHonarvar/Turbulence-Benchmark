
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    
    for i in range(m):
        for j in range(n):
            if matrix[i, j] == 93:
                for k in range(i+1, m+1):
                    for l in range(j+1, n+1):
                        submatrix = matrix[i:k, j:l]
                        if np.sum(submatrix) == 93 * submatrix.size:
                            count += 1
    
    return count
