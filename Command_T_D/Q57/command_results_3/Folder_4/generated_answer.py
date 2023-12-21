import numpy as np
def submatrix_with_particular_sum(mat):
    return [row[1:] for row in np.where(np.sum(row,axis=1)==87)[0]]
