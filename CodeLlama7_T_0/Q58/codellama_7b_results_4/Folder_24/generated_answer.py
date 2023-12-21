
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 49):
        for j in range(matrix.shape[1] - 49):
            if np.count_nonzero(matrix[i:i+50, j:j+50]) == 50:
                count += 1
    return count
