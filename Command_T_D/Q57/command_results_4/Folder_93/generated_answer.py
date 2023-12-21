import numpy as np
def submatrix_with_particular_sum(arr):
    m = len(arr)
    n = len(arr[0])
    l = []
    for i in range(m):
        for j in range(n):
            cnt = 0
            for k in range(i, m):
                for l in range(j, n):
                    cnt += arr[k][l]
            if cnt == -65:
                row = np.full((n,), -65)
                row[j] = arr[i][j]
                l.append(row)
    return l
