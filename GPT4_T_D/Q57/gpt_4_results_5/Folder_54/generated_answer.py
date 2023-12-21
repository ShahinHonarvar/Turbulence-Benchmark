
import numpy as np

def submatrix_with_particular_sum(two_d_matrix):
    shape = two_d_matrix.shape
    result = []

    for sub_size in range(1, min(shape) + 1):
        for top_corner_row in range(0, shape[0] - sub_size + 1):
            for top_corner_col in range(0, shape[1] - sub_size + 1):
                submatrix = two_d_matrix[top_corner_row:top_corner_row + sub_size, top_corner_col:top_corner_col + sub_size]
                if np.sum(submatrix) == -59:
                    result.append(submatrix)

    return result
