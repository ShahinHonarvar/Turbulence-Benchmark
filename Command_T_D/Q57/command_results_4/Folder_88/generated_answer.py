import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    return np.where(np.sum(matrix, axis=1) == -64)[0].tolist()
