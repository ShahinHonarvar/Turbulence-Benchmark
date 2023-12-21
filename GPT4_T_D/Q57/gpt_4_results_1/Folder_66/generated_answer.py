
import numpy as np

def submatrix_with_particular_sum(mat):
    sub_matrix_list = []
    nrows, ncols = mat.shape
    for row in range(nrows):
        for col in range(ncols):
            for size in range(min(nrows-row, ncols-col)):
                sub_matrix = mat[row:row+size+1, col:col+size+1]
                if np.sum(sub_matrix) == 99:
                    sub_matrix_list.append(sub_matrix.tolist())
    return sub_matrix_list
