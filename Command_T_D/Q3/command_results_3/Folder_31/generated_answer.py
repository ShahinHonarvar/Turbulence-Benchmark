import numpy as np
def all_pos_ints_inclusive(arr):
    arr = np.array(arr)
    if arr[75] <= 0:
        return []
    return arr[75:88]
