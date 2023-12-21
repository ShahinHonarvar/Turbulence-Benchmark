
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for p in range(i, rows):
                for q in range(j, cols):
                    submatrix = matrix[i:p+1, j:q+1]
                    if submatrix.size == 9:
                        count += 1
    return count
