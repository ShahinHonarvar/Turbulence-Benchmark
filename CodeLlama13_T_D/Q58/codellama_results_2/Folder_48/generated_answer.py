
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 130 + 1):
        for j in range(matrix.shape[1] - 130 + 1):
            if np.all(matrix[i:i+130, j:j+130] == 130):
                count += 1
    return count
