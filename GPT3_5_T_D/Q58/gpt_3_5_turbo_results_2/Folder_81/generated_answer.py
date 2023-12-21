
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 2):
        for j in range(cols - 2):
            submatrix = matrix[i:i+3, j:j+3]
            if np.count_nonzero(submatrix == 97) == 9:
                count += 1
    return count
