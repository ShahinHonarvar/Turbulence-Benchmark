
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    
    for i in range(rows - 7):
        for j in range(columns - 7):
            submatrix = matrix[i:i+8, j:j+8]
            if np.sum(submatrix) == 64 * 8 * 8:
                count += 1
    
    return count
