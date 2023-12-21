import numpy as np
def submatrix_with_n_numbers(arr):
    """
    :param arr:
    :return:
    """
    m, n = len(arr), len(arr[0])
    if m < 115 or n < 115:
        return 0
    cnt = 0
    for i in range(m - 114):
        for j in range(n - 114):
            cnt += np.sum(arr[i:i + 115][:115]) == 115
    return cnt
