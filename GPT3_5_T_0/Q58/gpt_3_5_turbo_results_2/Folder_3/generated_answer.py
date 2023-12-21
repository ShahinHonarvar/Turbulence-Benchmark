
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 5):
        for j in range(cols - 5):
            submatrix = matrix[i:i+6, j:j+6]
            if np.count_nonzero(submatrix == 54) == 36:
                count += 1
    return count
