
import numpy as np


def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            for p in range(i, rows):
                for q in range(j, cols):
                    submatrix = matrix[i:p + 1, j:q + 1]
                    if submatrix.size == 166:
                        count += 1

    return count
