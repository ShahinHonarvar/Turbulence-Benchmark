
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + 5 <= matrix.shape[0] and j + 5 <= matrix.shape[1]:
                submatrix = matrix[i:i+5, j:j+5]
                if np.sum(submatrix) == 54:
                    count += 1
    return count
