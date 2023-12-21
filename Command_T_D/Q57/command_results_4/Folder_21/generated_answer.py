import numpy as np
def submatrix_with_particular_sum(np_matrix):
    np_matrix_ = np_matrix.copy()
    empty_list = []
    for row in range(np_matrix.shape[0]):
        for col in range(np_matrix.shape[1]):
            np_matrix[row][col] = -936
            if np.all(np_matrix == -936):
                yield np_matrix
            np_matrix[row][col] = np_matrix_[row][col]
    if np_matrix == -936:
        yield np_matrix
