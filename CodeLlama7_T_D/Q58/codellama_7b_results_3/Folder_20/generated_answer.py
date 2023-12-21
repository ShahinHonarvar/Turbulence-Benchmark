
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.count_nonzero(submatrix == 49) == 4:
                count += 1

    return count
