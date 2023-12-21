
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target = 57
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == target and submatrix.size == target:
                        count += 1
    return count
