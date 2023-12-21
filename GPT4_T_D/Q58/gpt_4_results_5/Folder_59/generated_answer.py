
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r1 in range(rows):
        for r2 in range(r1 +1, rows + 1):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols + 1):
                    if (r2-r1) * (c2-c1) == 76:
                        count += 1
    return count
