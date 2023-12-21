
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    for i in range(nrows):
        for j in range(ncols):
            if matrix[i, j] == 59:
                for k in range(i+1, nrows+1):
                    for l in range(j+1, ncols+1):
                        submatrix = matrix[i:k, j:l]
                        if np.sum(submatrix == 59) == 59:
                            count += 1
    return count
