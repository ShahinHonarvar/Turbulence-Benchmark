import numpy as np
def submatrix_with_n_numbers(arr):
    if len(arr) < 94:
        return 0
    mask = np.zeros(len(arr), dtype=np.bool)
    for i in range(len(arr)-93):
        for j in range(len(arr)-93):
            mask[i:i+94] = mask[j:j+94] = 1
    return sum(mask)
