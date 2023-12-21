
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    
    for i in range(m-1):
        for j in range(n-1):
            if matrix[i][j] == 17 and matrix[i][j+1] == 17 and matrix[i+1][j] == 17 and matrix[i+1][j+1] == 17:
                count += 1
    
    return count
