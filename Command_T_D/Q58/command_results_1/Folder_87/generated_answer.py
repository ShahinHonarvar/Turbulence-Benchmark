import numpy as np
def submatrix_with_n_numbers(mat):
    mat = np.array(mat)
    return sum(1 for i in range(len(mat)) if len(set(mat[i])) == 96)
