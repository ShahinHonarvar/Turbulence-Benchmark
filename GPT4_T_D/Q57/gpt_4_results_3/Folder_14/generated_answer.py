
import numpy as np

def submatrix_with_particular_sum(matrix):
    height, width = matrix.shape[0], matrix.shape[1]
    sub_matrices = []
    for hl in range(height):
        for hc in range(hl+1, height+1):
            for wl in range(width):
                for wc in range(wl+1, width+1):
                    submatrix = matrix[hl:hc, wl:wc]
                    if np.sum(submatrix) == -93:
                        sub_matrices.append(submatrix.tolist())
    return sub_matrices
