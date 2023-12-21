
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    sub_matrices = []

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):

            for row in range(0, rows - i + 1):
                for col in range(0, cols - j + 1):

                    sub_mat = mat[row:row + i, col:col + j]

                    if np.sum(sub_mat) == -308:
                        sub_matrices.append(sub_mat)

    return sub_matrices
