
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix = matrix[i:i+2, j:j+2]
            if np.sum(submatrix) == 24:
                count += 1
    return count
