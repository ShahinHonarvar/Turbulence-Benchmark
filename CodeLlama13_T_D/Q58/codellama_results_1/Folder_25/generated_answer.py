
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 66
    count = 0
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            submat = matrix[i:i+n, j:j+n]
            if np.all(submat == n):
                count += 1
    return count
