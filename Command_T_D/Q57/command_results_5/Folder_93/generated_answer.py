def submatrix_with_particular_sum(arr):
    return [sub for i in range(len(arr) - 1) for j in range(len(arr[0]) - 1) for sub in arr[i][j:].split()]
