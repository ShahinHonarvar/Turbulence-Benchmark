
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 176:
                for k in range(i, rows):
                    for l in range(j, cols):
                        if np.sum(matrix[i:k+1, j:l+1]) == 176:
                            count += 1
    return count
