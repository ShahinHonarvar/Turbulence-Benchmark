
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    sub_matrices = []
    
    for sub_m in range(1, m+1):
        for sub_n in range(1, n+1):
            for row in range(m-sub_m+1):
                for col in range(n-sub_n+1):
                    sub_matrix = matrix[row:row+sub_m, col:col+sub_n]
                    if np.sum(sub_matrix) == 54:
                        sub_matrices.append(sub_matrix)
    return sub_matrices
