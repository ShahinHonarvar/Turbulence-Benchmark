import numpy as np
def submatrix_with_particular_sum(matrix):
    return np.where(matrix == -13, matrix, np.nan).tolist()
