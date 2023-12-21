import numpy as np
def submatrix_with_particular_sum(matrix):
    return [x for x in np.array_split(matrix, 15, axis=1) if len(x) == len(matrix) and x.sum(axis=1) == 15]
