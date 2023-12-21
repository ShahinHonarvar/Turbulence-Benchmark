import numpy as np
def submatrix_with_n_numbers(mat):
    mat = np.array(mat)
    return mat.size // 57 * mat.size // 57 - np.sum(mat[0:57] != np.matrix(range(57)), axis=1).sum() - np.sum(mat[-57:] != np.matrix(range(57)), axis=1).sum()
