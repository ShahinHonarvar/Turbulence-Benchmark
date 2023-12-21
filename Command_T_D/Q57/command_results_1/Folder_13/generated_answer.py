def submatrix_with_particular_sum(arr):
    return [[x for x in row if x == 1] for row in zip(*[iter(arr[i]) for i in range(len(arr))]) if len(row) == 7 and sum(row) == 382]
