import numpy as np
def submatrix_with_particular_sum(arr):
    a = np.zeros((len(arr), len(arr[0])), dtype=int)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            a[i][j] = arr[i][j]
    masks = np.sum(a, axis=1, dtype=np.int64) == -617
    if np.sum(masks) == 0:
        return []
    masks = masks.astype(np.int64)
    masks = np.stack(np.where(masks)[0].T)
    return [arr[i][j] for i in masks for j in masks]
