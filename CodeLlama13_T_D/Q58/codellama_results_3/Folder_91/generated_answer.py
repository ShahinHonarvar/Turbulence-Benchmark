
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    rows, cols = matrix.shape
    count = 0
    
    for i in range(rows-4):
        for j in range(cols-4):
            submat = matrix[i:i+5, j:j+5]
            if np.count_nonzero(submat == submat.flat[0]) == 25:
                count += 1
    
    return count
