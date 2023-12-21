def submatrix_with_particular_sum(arr):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 901:
                result += [[arr[i][:j] + arr[i][j + 1 :]]
    return result
