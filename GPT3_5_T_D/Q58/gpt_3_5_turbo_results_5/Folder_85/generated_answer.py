
import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    rows, cols = matrix.shape

    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix = matrix[i:i+2, j:j+2]
            if np.sum(submatrix) == 13:
                submatrix_count += 1

    return submatrix_count
