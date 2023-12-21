
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 76):
        for j in range(matrix.shape[1] - 76):
            if np.all(matrix[i:i+77, j:j+77] == 77)):
                count += 1

    return count
