
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 169):
        for j in range(matrix.shape[1] - 169):
            if np.all(matrix[i:i+179, j:j+179] == 179)):
                count += 1

    return count
