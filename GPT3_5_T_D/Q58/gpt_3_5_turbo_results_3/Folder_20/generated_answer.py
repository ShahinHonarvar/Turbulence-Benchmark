
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for i in range(rows - 6):
        for j in range(cols - 6):
            submatrix = matrix[i:i+7, j:j+7]
            if np.count_nonzero(submatrix == 49) == 49:
                count += 1

    return count
