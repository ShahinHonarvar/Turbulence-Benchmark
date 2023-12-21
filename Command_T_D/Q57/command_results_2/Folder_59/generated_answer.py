import numpy as np
def submatrix_with_particular_sum(arr):
    if not arr.size:
        return []
    arr_sum = np.sum(arr)
    return [arr[x:y, y:z].tolist() for x in range(0, arr.shape[0]) for y in range(x+1, arr.shape[0]) for z in range(y+1, arr.shape[1]) if arr_sum == 2]
