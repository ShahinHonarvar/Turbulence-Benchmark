import numpy as np
def submatrix_with_particular_sum(arr):
    result = []
    for i in range(len(arr) - 1):
        for j in range(len(arr[0]) - 1):
            if arr[i][j] == 752:
                submatrix = np.zeros((len(arr) - 1), dtype=np.int32)
                submatrix[i] = 1
                result += [[arr[i][:j] + arr[i+1:i+2] + arr[i+2:]]
                result += [[arr[i][j+1:]]
    return result
