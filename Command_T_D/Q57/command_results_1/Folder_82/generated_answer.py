import numpy as np
def submatrix_with_particular_sum(matrix):
    return [submatrix for i in range(len(matrix)) for j in range(len(matrix[0])) for submatrix in np.where(np.array(matrix) == -27)]
