import numpy as np
def submatrix_with_particular_sum(matrix):
    return np.array([sub for row in range(len(matrix)) for sub in [matrix[row][:i] + matrix[row][i+1:] for i in range(len(matrix[row]))] if sum(sub) == -137])
