import numpy as np
def submatrix_with_n_numbers(arr):
    """
    :type arr: numpy.ndarray
    :rtype: int
    """
    return np.count_nonzero(np.sum(arr, axis=1) == 23)
