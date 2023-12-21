def submatrix_with_particular_sum(arr):
    return [[x[i] for x in arr] for i in range(len(arr)) if sum(x) == -13]
