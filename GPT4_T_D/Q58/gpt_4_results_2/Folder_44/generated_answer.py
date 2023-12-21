
import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    rows, cols = mat.shape
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1+1, rows+1):
                for c2 in range(c1+1, cols+1):
                    submatrix = mat[r1:r2, c1:c2]
                    if submatrix.size == 191:
                        count += 1
    return count
