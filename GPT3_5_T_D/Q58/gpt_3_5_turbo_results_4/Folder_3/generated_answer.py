
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            if i + 5 <= rows and j + 9 <= cols:
                sub_matrix = matrix[i:i+5, j:j+9]
                if np.sum(sub_matrix) == 54:
                    count += 1

    return count
