
import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrices = []
    n, m = matrix.shape
    for sub_n in range(1, n+1):
        for sub_m in range(1, m+1):
            for row in range(n - sub_n + 1):
                for col in range(m - sub_m + 1):
                    sub_matrix = matrix[row:row + sub_n, col:col + sub_m]
                    if np.sum(sub_matrix) == -93:
                        sub_matrices.append(sub_matrix)
    return sub_matrices
