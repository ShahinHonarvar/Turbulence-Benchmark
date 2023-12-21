def submatrix_with_particular_sum(arr):
    sm = [[0]*arr.shape[1]]
    sm[0][0] = arr[0][0]
    for i in range(1, arr.shape[0]):
        sm.append([0]*arr.shape[1])
        sm[-1][0] = arr[-1][0]
        for j in range(1, arr.shape[1]):
            sm[-1][j] = arr[-1][j] + sm[-2][j-1]
    return [s for s in zip(*sm)]
