
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 6):
        for j in range(len(matrix[0]) - 6):
            submatrix = matrix[i:i+7, j:j+7]
            if np.size(submatrix) == 49:
                count += 1
    return count
