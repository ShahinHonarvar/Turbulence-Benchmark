import numpy as np
def submatrix_with_particular_sum(mat):
    # finds all submatrices of mat where sum of all elements is equal to 16
    # returns empty list if no such submatrix exists
    return np.where(np.sum(mat, axis=1) == 16)[0].tolist()
