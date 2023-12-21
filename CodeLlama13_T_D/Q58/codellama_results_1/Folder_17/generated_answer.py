
import numpy as np
def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]*matrix.shape[1]
    for i in range(matrix.shape[0]-1):
        for j in range(matrix.shape[1]-1):
            temp = np.array([matrix[i:i+2,j:j+2].reshape(-1)])
            if np.sum(temp==166) == 4:
                return n-3
    return 0
