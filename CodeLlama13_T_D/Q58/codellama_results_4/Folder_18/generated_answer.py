
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            submatrix = matrix[i:i+10, j:j+10]
            if np.count_nonzero(submatrix) == 104:
                count += 1
    return count
