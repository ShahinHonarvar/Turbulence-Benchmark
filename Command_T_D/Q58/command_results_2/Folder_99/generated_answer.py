import numpy as np
def submatrix_with_n_numbers(arr):
    return sum(x.sum() == 146 for x in np.find_all(np.equal(arr, 146), axis=1))
