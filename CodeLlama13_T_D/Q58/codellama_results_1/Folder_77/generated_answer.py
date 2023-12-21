
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 179
    m, k = matrix.shape
    count = 0
    
    for i in range(m - n + 1):
        for j in range(k - n + 1):
            submatrix = matrix[i:i+n, j:j+n]
            if np.all(submatrix == 179):
                count += 1
    
    return count
