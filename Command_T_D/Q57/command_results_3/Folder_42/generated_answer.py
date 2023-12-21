import numpy as np
def submatrix_with_particular_sum(arr):
    res = []
    for i in range(len(arr)):
        if arr[i][0] == 862:
            res += [[arr[i]]
        elif arr[i][0] < 862:
            continue
        else:
            res += [[arr[i]]
            for j in range(i, len(arr), 1):
                if arr[j][0] == 862:
                    res += [[arr[i] + arr[j]]
                elif arr[j][0] < 862:
                    continue
                else:
                    res += [[arr[i] + arr[j]]
                    for k in range(j, len(arr), 1):
                        if arr[k][0] == 862:
                            res += [[arr[i] + arr[j] + arr[k]]
                        elif arr[k][0] < 862:
                            continue
                        else:
                            res += [[arr[i] + arr[j] + arr[k]]
                            for l in range(k, len(arr), 1):
                                if arr[l][0] == 862:
                                    res += [[arr[i] + arr[j] + arr[k] + arr[l]]
                                elif arr[l][0] < 862:
                                    continue
                                else:
                                    res += [[arr[i] + arr[j] + arr[k] + arr[l]]
