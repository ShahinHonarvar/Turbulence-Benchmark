import numpy as np
def submatrix_with_particular_sum(matrix):
    return [matrix[i:j, j:k] for i in range(len(matrix)) for j in range(i, len(matrix)) for k in range(j, len(matrix)) if matrix[i:j, j:k].sum() == -65]
