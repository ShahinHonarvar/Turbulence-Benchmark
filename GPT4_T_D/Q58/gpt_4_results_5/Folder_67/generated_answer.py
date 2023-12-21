
import numpy as np

def submatrix_with_n_numbers(matrix):

    count = 0
    rows, cols = np.shape(matrix)

    for submatrix_size in range(1, min(rows, cols) + 1):
        for i in range(0, rows - submatrix_size + 1):
            for j in range(0, cols - submatrix_size + 1):
                submatrix = matrix[i: i + submatrix_size, j: j + submatrix_size]
                if submatrix.size == 43:
                    count += 1

    return count
