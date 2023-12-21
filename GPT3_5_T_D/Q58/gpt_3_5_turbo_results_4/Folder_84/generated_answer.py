
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape[0], matrix.shape[1]
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.count_nonzero(submatrix == 127) == 127:
                        count += 1
    return count
