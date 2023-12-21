
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for r in range(row):
        for c in range(col):
            for i in range(r, row):
                for j in range(c, col):
                    submatrix = matrix[r:i+1, c:j+1]
                    if submatrix.size == 191:
                        count += 1
    return count
