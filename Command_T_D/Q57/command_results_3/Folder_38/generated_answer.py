import numpy as np
def submatrix_with_particular_sum(matrix):
    return [x for x in np.split(matrix, np.where(np.sum(x, axis=1) == 34)[0]) if len(x) > 0]
