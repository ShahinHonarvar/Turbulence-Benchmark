
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    sub_matrix_list = []

    for size_i in range(1, m+1):
        for size_j in range(1, n+1):
            for i in range(m - size_i + 1):
                for j in range(n - size_j + 1):
                    sub_matrix = matrix[i:i+size_i, j:j+size_j]
                    if np.sum(sub_matrix) == 432:
                        sub_matrix_list.append(sub_matrix)
    return sub_matrix_list
