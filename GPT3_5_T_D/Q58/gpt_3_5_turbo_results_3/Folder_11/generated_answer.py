
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 38:
                for k in range(i, rows):
                    for l in range(j, cols):
                        if np.sum(matrix[i:k+1, j:l+1]) == 38 * (k - i + 1) * (l - j + 1):
                            count += 1
    return count
