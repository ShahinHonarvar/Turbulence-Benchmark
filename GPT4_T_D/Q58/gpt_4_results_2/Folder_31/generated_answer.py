
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row_size, col_size = matrix.shape
    for r in range(row_size):
        for c in range(col_size):
            for x in range(r, row_size):
                for y in range(c, col_size):
                    submatrix = matrix[r:x+1, c:y+1]
                    if submatrix.size == 45:
                        count += 1
    return count
