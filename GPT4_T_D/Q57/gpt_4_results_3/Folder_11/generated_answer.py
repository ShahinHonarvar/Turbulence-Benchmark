
import numpy as np

def sub_matrix_with_sum(mat):
    row, col = len(mat), len(mat[0])
    sub_matrices = []
    
    for row_size in range(1, row + 1):
        for col_size in range(1, col + 1):
            for i in range(0, row - row_size + 1):
                for j in range(0, col - col_size + 1):
                    sub_matrix = mat[i : i + row_size, j : j + col_size]
                    if np.sum(sub_matrix) == 38:
                        sub_matrices.append(sub_matrix)
    return sub_matrices

def submatrix_with_particular_sum(mat):
    if isinstance(mat, np.ndarray):
        return sub_matrix_with_sum(mat)
    return []
