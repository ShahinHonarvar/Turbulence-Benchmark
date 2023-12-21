import numpy as np
def submatrix_with_n_numbers(arr):
    res = 0
    for r in range(len(arr) - 1):
        for c in range(len(arr[0]) - 1):
            x = arr[r][c]
            cnt = 1
            while r + cnt < len(arr) and c + cnt < len(arr[0]):
                if arr[r + cnt][c + cnt] == x:
                    cnt += 1
                else:
                    break
            if cnt == 16:
                res += 1
    return res
