
import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    rows, columns = matrix.shape
    for i in range(rows-3+1):
        for j in range(columns-4+1):
            submatrix = matrix[i:i+3, j:j+4]
            if np.sum(submatrix) == 96:
                submatrix_count += 1
    return submatrix_count
