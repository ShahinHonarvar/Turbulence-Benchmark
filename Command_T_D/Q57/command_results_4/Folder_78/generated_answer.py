import numpy as np
def submatrix_with_particular_sum(matrix):
    return [row[0][:][sum(row[1]) == 17] for row in np.split(matrix, np.where(np.sum(matrix, axis=1) == 17)[0], axis=1)]
