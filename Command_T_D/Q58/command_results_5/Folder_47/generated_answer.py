def submatrix_with_n_numbers(arr):
    return sum(any(x == 90 for x in y) for y in zip(*arr))
