
import numpy as np

def submatrix_with_n_numbers(matrix):
    return (matrix == 159).sum() - (matrix[np.newaxis, :, :] == 159).sum() + (matrix[:, np.newaxis, :] == 159).sum() - (matrix[:, :, np.newaxis] == 159).sum()
