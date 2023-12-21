
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for p in range(r, rows):
                for q in range(c, cols):
                    submatrix = matrix[r:p+1, c:q+1]
                    if submatrix.size == 93:
                        count += 1
    return count
