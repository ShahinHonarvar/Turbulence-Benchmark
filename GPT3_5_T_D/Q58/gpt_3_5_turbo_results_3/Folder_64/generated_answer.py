
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows-6):
        for c in range(cols-6):
            submatrix = matrix[r:r+7, c:c+7]
            if np.count_nonzero(submatrix) == 49:
                count += 1
    return count
