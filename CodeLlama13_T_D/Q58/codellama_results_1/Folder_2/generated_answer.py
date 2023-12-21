
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 106):
        for j in range(cols - 106):
            submatrix = matrix[i:i+107, j:j+107]
            if np.sum(submatrix) == 107 * 107:
                count += 1
    return count
