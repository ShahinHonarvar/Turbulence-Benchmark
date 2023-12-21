
import numpy as np
def submatrix_with_n_numbers(mat):
    n = 87
    return np.sum(np.array([np.all(row == n) for row in mat])) + np.sum(np.array([np.all(col == n) for col in np.transpose(mat)]))
