
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 193
    count = 0
    m, n = matrix.shape
    
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix = matrix[i:k+1, j:l+1]
                    if submatrix.size == n * n and np.sum(submatrix) == n * n * n:
                        count += 1
    
    return count
