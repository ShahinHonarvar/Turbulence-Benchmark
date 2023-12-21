import numpy as np
def submatrix_with_particular_sum(matrix):
    return [x for x in np.where(np.sum(matrix[i:j+1], axis=1) == 59) if x]
