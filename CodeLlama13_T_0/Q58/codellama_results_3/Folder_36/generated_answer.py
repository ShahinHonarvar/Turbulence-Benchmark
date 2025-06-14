
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 131
    count = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            submatrix = matrix[i:i+n, j:j+n]
            if np.sum(submatrix == 1) == n:
                count += 1
    return count
