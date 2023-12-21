
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for i in range(rows - 9):
        for j in range(cols - 9):
            submatrix = matrix[i:i+10, j:j+10]
            if np.count_nonzero(submatrix == 85) == 85:
                count += 1
    
    return count
