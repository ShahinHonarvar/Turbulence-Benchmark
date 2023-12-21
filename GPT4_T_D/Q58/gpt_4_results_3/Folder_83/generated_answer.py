
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r1 in range(rows):
        for r2 in range(r1+1, rows+1):
            for c1 in range(cols):
                for c2 in range(c1+1, cols+1):
                    sub_matrix = matrix[r1:r2, c1:c2]
                    if sub_matrix.size == 47:
                        count += 1
    return count
