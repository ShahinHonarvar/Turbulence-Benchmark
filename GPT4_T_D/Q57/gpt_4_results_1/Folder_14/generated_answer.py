
import numpy as np

def submatrix_with_particular_sum(matrix):

    num_rows = matrix.shape[0]
    num_cols = matrix.shape[1]
    submatrices = []
    result = []

    for sub_mat_size in range(1, min(num_rows, num_cols) + 1):
        for x in range(0, num_rows - sub_mat_size + 1):
            for y in range(0, num_cols - sub_mat_size + 1):
                subm = matrix[x:x + sub_mat_size, y:y + sub_mat_size]
                submatrices.append(subm)

    for i in submatrices:
        if np.sum(i) == -93:
            result.append(i)

    return result
