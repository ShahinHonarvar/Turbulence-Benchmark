import numpy as np
def submatrix_with_particular_sum(arr):
    if arr.shape[0] < 6:
        return []
    mask = np.full((arr.shape[0], arr.shape[1]), True)
    for i in range(len(mask)):
        mask[i][:i] = False
        mask[i][i+1:] = False
    return [submatrix for submatrix in zip(*mask.nonzero()) if sum(submatrix) == 92]
