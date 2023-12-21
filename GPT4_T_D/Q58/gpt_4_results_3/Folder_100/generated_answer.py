
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = np.shape(matrix)
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if r * c == 10:
                count += (rows - r + 1) * (cols - c + 1)
    return count
