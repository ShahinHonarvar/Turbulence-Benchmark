import numpy as np
def submatrix_with_particular_sum(mat):
    return [x for x in np.where(np.all(mat == 0, axis=1))[0] if len(x) > 0]
