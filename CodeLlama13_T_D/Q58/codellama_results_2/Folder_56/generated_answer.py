
import numpy as np
def submatrix_with_n_numbers(mat, n):
    return sum(np.sum(mat == n))
