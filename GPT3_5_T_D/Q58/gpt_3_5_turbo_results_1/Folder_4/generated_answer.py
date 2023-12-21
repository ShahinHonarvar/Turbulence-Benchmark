
import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    
    for i in range(row - 1):
        for j in range(col - 1):
            if matrix[i:i + 2, j:j + 2].size == 4 and np.sum(matrix[i:i + 2, j:j + 2] == 15) == 4:
                count += 1
                
    return count
