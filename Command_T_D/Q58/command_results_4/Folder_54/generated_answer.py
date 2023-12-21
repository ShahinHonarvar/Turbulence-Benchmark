import numpy as np
def submatrix_with_n_numbers(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            s = np.array([arr[i][j]])
            n = 27
            cnt = 0
            while n:
                if not s.size():
                    break
                cnt += 1
                if cnt == n:
                    break
                s = np.concatenate((s, s[1:]))
                n -= 1
            if cnt == n:
                res += 1
    return res
