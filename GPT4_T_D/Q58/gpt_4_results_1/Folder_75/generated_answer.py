
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for x in range(r, rows):
                for y in range(c, cols):
                    if (x - r + 1) * (y - c + 1) == 80:
                        count += 1
    return count
