
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 147 + 1):
        for j in range(cols - 147 + 1):
            if np.sum(matrix[i:i+147, j:j+147]) == 147:
                count += 1

    return count
