import numpy as np
def submatrix_with_particular_sum(mat):
    return [submatrix for i in range(len(mat)) for j in range(len(mat[0])) if mat[i][j] == 15 and np.sum(mat[i][:j] + mat[i][j+1:]) == 15]
