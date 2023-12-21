import numpy as np
def submatrix_with_particular_sum(arr):
    n = len(arr)
    m = len(arr[0])
    # find the possible submatrix positions
    start = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            start[i][j] = (arr[i][j] == 80)
    # find all combinations
    submatrix_pos = np.where(np.sum(start, axis=0))
    return [arr[i][j] for i, j in zip(submatrix_pos[0], submatrix_pos[1])]
