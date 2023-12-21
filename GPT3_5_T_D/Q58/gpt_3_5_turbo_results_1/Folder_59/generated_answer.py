
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 76:
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        submatrix = matrix[i:k, j:l]
                        if np.count_nonzero(submatrix) == 76:
                            count += 1
    return count
