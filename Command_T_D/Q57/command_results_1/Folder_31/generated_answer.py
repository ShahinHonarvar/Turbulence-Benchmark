import numpy as np
def submatrix_with_particular_sum(matrix):
    # Write your code here
    if matrix.shape[0] == 1:
        return []
    if matrix.shape[1] == 1:
        return []
    return [np.sum(matrix[i:j+1], axis=0) == -44 for i in range(len(matrix) - 1) for j in range(i + 1, len(matrix))]
