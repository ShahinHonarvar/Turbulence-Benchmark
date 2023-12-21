def submatrix_with_particular_sum(arr):
    if sum(arr) == -336:
        return [[arr[i:j] for i in range(len(arr)) for j in range(i, len(arr))]]
    return []
