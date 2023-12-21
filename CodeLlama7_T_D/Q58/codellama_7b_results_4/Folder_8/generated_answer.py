
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            if matrix[i][j] == 29:
                for k in range(i, i + 2):
                    for l in range(j, j + 2):
                        if matrix[k][l] == 29:
                            count += 1

    return count
