
import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size == 0:
        return 0
    
    count = 0
    rows, cols = matrix.shape
    submatrix_size = 138

    for i in range(rows - submatrix_size + 1):
        for j in range(cols - submatrix_size + 1):
            submatrix = matrix[i:i+submatrix_size, j:j+submatrix_size]
            if np.count_nonzero(submatrix == 138) == submatrix_size ** 2:
                count += 1
    
    return count
