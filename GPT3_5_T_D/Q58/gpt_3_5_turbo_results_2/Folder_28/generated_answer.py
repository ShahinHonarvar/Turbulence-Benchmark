
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            sub_matrix = matrix[i:i+2, j:j+2]
            if np.sum(sub_matrix) == 37:
                count += 1
    return count
