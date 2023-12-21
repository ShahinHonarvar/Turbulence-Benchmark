
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    count = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            submat = matrix[i:i+n, j:j+n]
            if np.all(submat == n):
                count += 1
    return count
