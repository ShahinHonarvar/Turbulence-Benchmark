import numpy as np
def submatrix_with_particular_sum(matrix):
    if not matrix.flags['OWNDATA']:
        matrix = np.array(matrix)
    return [np.array(x) for x in np.nditer(matrix, flags=['READONLY'], op_diffs=True) if np.sum(x) == 38]
