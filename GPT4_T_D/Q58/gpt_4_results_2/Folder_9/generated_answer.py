
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for x in range(r+1, rows+1):
                for y in range(c+1, cols+1):
                    if np.size(matrix[r:x, c:y]) == 33:
                        count += 1
    return count
