def submatrix_with_particular_sum(arr):
    return [[x[i][j] for x in arr if sum(x) == 93] for i in range(len(arr)) for j in range(len(arr[0]))]
