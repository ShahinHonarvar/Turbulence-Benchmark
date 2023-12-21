
import numpy as np

def submatrix_with_particular_sum(np_matrix):

    sub_matrices = []
    dim_x, dim_y = np_matrix.shape

    for x in range(1, dim_x+1):
        for y in range(1, dim_y+1):
            for i in range(dim_x-x+1):
                for j in range(dim_y-y+1):
                    sub_matrix = np_matrix[i:i+x, j:j+y]
                    if np.sum(sub_matrix) == 95:
                        sub_matrices.append(sub_matrix)

    return sub_matrices
