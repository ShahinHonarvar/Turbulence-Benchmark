import numpy as np
def submatrix_with_particular_sum(matrix):
    # Your code here
    matrix = np.array(matrix)
    return np.where(np.sum(matrix, axis=1) == 77)[0]
