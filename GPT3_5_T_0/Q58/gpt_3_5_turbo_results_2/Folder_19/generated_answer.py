
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 3):
        for j in range(cols - 3):
            submatrix = matrix[i:i+4, j:j+4]
            if np.count_nonzero(submatrix == 17) == 16:
                count += 1
    return count
