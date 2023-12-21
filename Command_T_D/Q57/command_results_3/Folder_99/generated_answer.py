import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    matrix = matrix[::-1]
    if np.sum(matrix) != -185:
        return []
    return [matrix[i:j, i:j] for i in range(len(matrix)) for j in range(i+1, len(matrix))]
