
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrices = []
    for sub_matrix_size in range(1, min(rows, cols)+1):
        for i in range(rows-sub_matrix_size+1):
            for j in range(cols-sub_matrix_size+1):
                sub_matrix = matrix[i:i+sub_matrix_size, j:j+sub_matrix_size]
                if np.sum(sub_matrix) == 69:
                    sub_matrices.append(sub_matrix)
    if len(sub_matrices) > 0:
        return sub_matrices
    else:
        return []
