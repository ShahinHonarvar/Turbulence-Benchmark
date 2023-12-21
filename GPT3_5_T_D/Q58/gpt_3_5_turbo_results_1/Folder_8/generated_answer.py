
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for r in range(rows):
        for c in range(cols):
            for i in range(r, rows):
                for j in range(c, cols):
                    submatrix = matrix[r:i+1, c:j+1]
                    if np.count_nonzero(submatrix == 29) == 29:
                        count += 1

    return count
