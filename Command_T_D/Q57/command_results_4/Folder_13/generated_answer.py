def submatrix_with_particular_sum(arr):
    return [[*row] for row in arr if sum(row) == 382]
