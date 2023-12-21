
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape

    for i in range(nrows - 9):
        for j in range(ncols - 9):
            submatrix = matrix[i:i+10, j:j+10]
            if np.count_nonzero(submatrix == 95) == 100:
                count += 1

    return count
