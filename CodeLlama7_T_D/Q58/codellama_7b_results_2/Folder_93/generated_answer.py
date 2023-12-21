
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 52):
        for j in range(matrix.shape[1] - 52):
            if (np.sum(matrix[i:i + 53, j:j + 53]) == 53 * 53) and not np.any((matrix[i:i + 53, j:j + 53] > 1))):
                count += 1

    return count
