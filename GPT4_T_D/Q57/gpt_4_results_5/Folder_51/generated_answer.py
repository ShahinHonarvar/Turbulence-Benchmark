
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    sub_matrices = []
    for sub_m in range(m+1):
        for sub_n in range(n+1):
            for row in range(m-sub_m+1):
                for col in range(n-sub_n+1):
                    sub_matrix = matrix[row:row+sub_m, col:col+sub_n]
                    if np.sum(sub_matrix) == -46:
                        sub_matrices.append(sub_matrix)
    return sub_matrices
