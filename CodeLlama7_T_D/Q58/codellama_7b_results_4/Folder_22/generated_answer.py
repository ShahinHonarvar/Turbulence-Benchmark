
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            if (np.count_nonzero(matrix[i] == 21) == matrix[i].size and np.count_nonzero(matrix[j] == 21) == matrix[j].size):
                count += 1

    return count
