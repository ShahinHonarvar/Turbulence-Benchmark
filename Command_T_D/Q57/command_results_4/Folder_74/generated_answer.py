def submatrix_with_particular_sum(arr):
    if sum(arr[0]) != 88:
        return []
    return [[arr[i:j+1] for i in range(0, len(arr)-1) for j in range(i+1, len(arr))]]
