
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for ro in range(r, rows):
                for co in range(c, cols):
                    submatrix = matrix[r:ro+1, c:co+1]
                    if submatrix.size == 7:
                        count += 1
    return count
