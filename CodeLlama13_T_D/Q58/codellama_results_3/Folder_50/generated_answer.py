
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 40
    count = 0
    
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            submat = matrix[i:i+n, j:j+n]
            if np.sum(submat == n) == n * n:
                count += 1
    
    return count
