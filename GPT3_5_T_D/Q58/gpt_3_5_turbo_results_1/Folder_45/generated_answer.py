
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 3 + 1):
        for j in range(cols - 3 + 1):
            sub_matrix = matrix[i:i+3, j:j+3]
            if np.sum(sub_matrix) == 28:
                count += 1
    return count
