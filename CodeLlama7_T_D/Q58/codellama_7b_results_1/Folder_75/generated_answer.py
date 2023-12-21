
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 80 + 1):
        for j in range(matrix.shape[1] - 80 + 1):
            if np.count_nonzero(matrix[i:i+80,j:j+80]) == 80:
                count += 1
    return count
