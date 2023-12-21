import numpy as np
def submatrix_with_particular_sum(arr):
    if not arr:
        return []
    m = arr.shape[0]
    n = arr.shape[1]
    r = []
    for i in range(m):
        for j in range(n):
            row = np.array(arr[i])
            col = np.array(arr[j])
            for k in range(m):
                for l in range(n):
                    if row[k] + col[l] == -81:
                        r.append(arr[i][:j] + arr[i][j+1:] + arr[k][:l] + arr[k][l+1:] + arr[j+1:][:])
                        break
    return r
