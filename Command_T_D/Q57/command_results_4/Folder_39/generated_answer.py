import numpy as np
def submatrix_with_particular_sum(mat):
    return np.where(mat == 66, mat, np.nan).tolist()
