import numpy as np
def submatrix_with_particular_sum(matrix):
    return [matrix[r][c] for r in range(len(matrix)) for c in range(len(matrix[0])) if np.sum(matrix[r][c]) == -57]
