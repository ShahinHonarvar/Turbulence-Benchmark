
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    
    for i in range(rows - 102):
        for j in range(cols - 102):
            submatrix = matrix[i:i+103, j:j+103]
            if np.sum(submatrix) == 103 * (103 + 1) // 2:
                count += 1
                
    return count
