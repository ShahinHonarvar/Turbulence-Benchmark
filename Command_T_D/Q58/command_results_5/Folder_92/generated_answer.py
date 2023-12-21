import numpy as np
def submatrix_with_n_numbers(mat):
    mat = np.array(mat)
    return sum(np.unique(np.where(np.all(mat[x] == mat[x+n], axis=0), row) + [x, x+n]) > 8 for x in range(0, len(mat)-7, 7))
