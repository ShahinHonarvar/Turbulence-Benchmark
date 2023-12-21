
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for x in range(r, rows):
                for y in range(c, cols):
                    if np.prod([x-r+1, y-c+1]) == 41:
                        count += 1
    return count
