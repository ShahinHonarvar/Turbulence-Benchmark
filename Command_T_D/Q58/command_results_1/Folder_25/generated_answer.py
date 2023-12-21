import numpy as np
def submatrix_with_n_numbers(mat):
    if mat.size == 0:
        return 0
    x = mat[0]
    y = mat[1]
    m = mat[2]
    return (mat.size - x) * (mat.size - y) * (mat.size - m)
