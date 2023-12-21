
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = np.shape(matrix)
    sub_matrices = []

    for row_size in range(1, rows + 1):
        for col_size in range(1, cols + 1):
            for row in range(rows - row_size + 1):
                for col in range(cols - col_size + 1):
                    sub_matrix = matrix[row:row + row_size, col:col + col_size]
                    if np.sum(sub_matrix) == 80:
                        sub_matrices.append(sub_matrix.tolist())

    return sub_matrices
