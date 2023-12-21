
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 1 < rows and j + 1 < cols:
                sub_matrix = matrix[i:i + 2, j:j + 2]
                if np.product(sub_matrix.shape) == 4:
                    count += 1
    return count
