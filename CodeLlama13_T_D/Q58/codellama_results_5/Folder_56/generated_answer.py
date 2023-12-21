
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    return (np.array_split(np.reshape(matrix, (-1, matrix.shape[1])), n) == n).sum()
