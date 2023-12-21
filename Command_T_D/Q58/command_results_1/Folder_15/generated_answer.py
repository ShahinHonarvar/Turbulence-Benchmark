def submatrix_with_n_numbers(arr):
    m, n = len(arr), len(arr[0])
    if m == 1:
        return arr[0] == [2]
    if n == 1:
        return arr[0] == [1]
    return arr[0] == [1] + submatrix_with_n_numbers(arr[1:])
