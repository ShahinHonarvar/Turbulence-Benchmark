import numpy as np
def submatrix_with_particular_sum(arr):
    a, b = np.where(arr == -90)
    return [arr[a[i]:b[i] + 1, j:j + len(a) + 1] for i in range(len(a))]
