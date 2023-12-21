import numpy as np
def submatrix_with_n_numbers(mat):
    return sum(any(np.all(mat[i][j] == 173) for i in range(len(mat) - 1)) for j in range(len(mat[0]) - 1))
