
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            submatrix = matrix[i:i+3, j:j+3].flatten()
            if len(submatrix) != 9:
                continue

            if np.sum(submatrix == 34) == 9:
                count += 1

    return count
