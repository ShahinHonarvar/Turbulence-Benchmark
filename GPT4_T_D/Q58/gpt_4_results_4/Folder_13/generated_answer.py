
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for r in range(row):
        for c in range(col):
            for i in range(1, row-r+1):
                for j in range(1, col-c+1):
                    sub_matrix = matrix[r:r+i, c:c+j]
                    if sub_matrix.size == 175:
                        count += 1
    return count
