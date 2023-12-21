
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 104 + 1):
        for j in range(len(matrix[i]) - 104 + 1):
            if np.count_nonzero(matrix[i:i+104, j:j+104]) == 104:
                count += 1
    return count
