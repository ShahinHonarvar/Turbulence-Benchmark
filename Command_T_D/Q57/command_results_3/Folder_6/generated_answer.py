import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    if not matrix.size:
        return []
    matrix = np.hstack((matrix, np.full(len(matrix), 126 - matrix.sum(axis=1))))
    return np.where(np.all(np.eye(len(matrix) + 1, 126 - matrix.sum(axis=1)) == np.hstack((matrix, np.full(len(matrix), 126 - matrix.sum(axis=1))), axis=1))[0]
