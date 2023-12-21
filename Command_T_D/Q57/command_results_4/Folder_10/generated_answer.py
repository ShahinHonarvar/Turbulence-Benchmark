import numpy as np
def submatrix_with_particular_sum(matrix):
    return [submatrix for i in range(len(matrix)) for j in range(len(matrix[i])) for submatrix in np.where(matrix[i][j] == 56)[0]]
