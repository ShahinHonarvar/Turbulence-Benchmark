
import numpy as np

def submatrix_with_particular_sum(input_matrix):
    matrices = []
    n, m = input_matrix.shape
    for row in range(n):
        for col in range(m):
            for row_size in range(1, n-row+1):
                for col_size in range(1, m-col+1):
                    submatrix = input_matrix[row:row + row_size, col:col + col_size]
                    if np.sum(submatrix) == -394:
                        matrices.append(submatrix)
    return matrices
