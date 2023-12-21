
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 126
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for row in range(r, rows):
                for col in range(c, cols):
                    if ((row + 1) - r) * ((col + 1) - c) == n:
                        count += 1
    return 0 if count == 0 else count
