import numpy as np
def submatrix_with_n_numbers(matrix):
    if matrix.shape[0] < 10 or matrix.shape[1] < 10:
        return 0
    return sum(sum(np.where(x == 185)[0]) for x in range(10, matrix.shape[0] + 1))
