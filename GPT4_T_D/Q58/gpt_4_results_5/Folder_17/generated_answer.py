
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    for size in range(1, min(nrows, ncols) + 1):
        for row in range(0, nrows - size + 1):
            for col in range(0, ncols - size + 1):
                submatrix = matrix[row:row + size, col:col + size]
                if np.size(submatrix) == 166:
                    count += 1
    return count
