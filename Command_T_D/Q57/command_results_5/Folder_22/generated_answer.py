import numpy as np
def submatrix_with_particular_sum(mat):
    return np.array([(i, j, mat[i][j]) for i in range(len(mat)) for j in range(len(mat[0])) if mat[i][j] == -38]).T
