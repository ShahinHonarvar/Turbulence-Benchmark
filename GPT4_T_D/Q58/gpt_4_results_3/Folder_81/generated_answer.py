
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for r1 in range(row):
        for r2 in range(r1+1, row+1):
            for c1 in range(col):
                for c2 in range(c1+1, col+1):
                    submatrix = matrix[r1:r2, c1:c2]
                    if submatrix.size == 97:
                        count += 1

    return count
