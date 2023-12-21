import numpy as np
def submatrix_with_particular_sum(mat):
    return [row for row in range(len(mat)) if np.sum(mat[row]) == -43]
