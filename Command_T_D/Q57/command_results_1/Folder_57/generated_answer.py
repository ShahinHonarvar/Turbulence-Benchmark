def submatrix_with_particular_sum(arr):
    return [[arr[x:x + n] for x in range(len(arr) - n)] for n in range(1, len(arr) + 1)]
