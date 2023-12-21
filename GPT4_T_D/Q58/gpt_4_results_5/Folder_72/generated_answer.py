
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(0, rows):
        for j in range(0, cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 16:
                        count += 1
    return count
