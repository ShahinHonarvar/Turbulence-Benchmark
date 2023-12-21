import numpy as np
def submatrix_with_particular_sum(arr):
    return [np.array(arr[start:start + size]).tolist() for start in range(0, len(arr) - size) for size in range(1, min(len(arr) - start, 5) + 1)]
