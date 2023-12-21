
import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.shape[0] < 3 or matrix.shape[1] < 3:
        return 0

    count = 0
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            submatrix = matrix[i:i+3, j:j+3]
            if np.count_nonzero(submatrix == 147) == 9:
                count += 1
    
    return count
