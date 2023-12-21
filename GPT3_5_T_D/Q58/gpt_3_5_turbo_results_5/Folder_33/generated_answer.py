
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 118:
                submatrix = matrix[i:, j:]
                sub_rows, sub_cols = submatrix.shape

                for k in range(sub_rows):
                    for l in range(sub_cols):
                        if submatrix[k, l] == 118 and (k + 1) * (l + 1) == 118:
                            count += 1

    return count
