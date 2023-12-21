def submatrix_with_particular_sum(arr):
    return [row for row in range(len(arr)) if sum(arr[row]) == -36]
