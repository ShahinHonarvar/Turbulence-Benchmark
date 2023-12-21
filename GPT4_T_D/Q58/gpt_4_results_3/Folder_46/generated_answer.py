
import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0

    row, col = matrix.shape
    count = 0

    for r in range(row):
        for c in range(col):
            for x in range(r, row):
                for y in range(c, col):
                    if (x - r + 1) * (y - c + 1) == 144:
                        count += 1

    return count
