
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            submatrix = matrix[i:i+66, j:j+66]
            if np.count_nonzero(submatrix) == 66:
                count += 1
    return count
