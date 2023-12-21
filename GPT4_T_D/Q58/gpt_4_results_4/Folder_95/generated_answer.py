
import numpy as np

def submatrix_with_n_numbers(matrix):
    num_of_submatrices = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.size(submatrix) == 87:
                        num_of_submatrices += 1
    return num_of_submatrices
