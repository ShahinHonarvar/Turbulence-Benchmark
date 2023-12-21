
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape

    for i in range(row - 50):
        for j in range(col - 50):
            submatrix = matrix[i:i+51, j:j+51]
            if np.count_nonzero(submatrix) == 51*51:
                count += 1

    return count
