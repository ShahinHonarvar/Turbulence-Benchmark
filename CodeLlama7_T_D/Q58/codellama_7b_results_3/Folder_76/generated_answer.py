
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 159 + 1):
        for j in range(matrix.shape[1] - 159 + 1):
            if np.all(matrix[i:i+159, j:j+159] == 159)):
                count += 1

    return count
