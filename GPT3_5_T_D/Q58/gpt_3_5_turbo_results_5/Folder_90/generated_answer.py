
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == 176:
                        count += 1
    
    return count
