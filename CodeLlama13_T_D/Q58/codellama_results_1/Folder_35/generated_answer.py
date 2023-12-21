
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                count = 0
                for k in range(i, rows):
                    for l in range(j, cols):
                        if matrix[k][l] == 1:
                            count += 1
                return count
    return 0
