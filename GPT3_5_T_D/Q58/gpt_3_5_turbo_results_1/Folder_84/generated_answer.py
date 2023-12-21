
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 127:
                for k in range(i, rows):
                    for l in range(j, cols):
                        submatrix = matrix[i:k+1, j:l+1]
                        if np.sum(submatrix) == 127 * submatrix.size:
                            count += 1
    return count
