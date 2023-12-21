def submatrix_with_n_numbers(arr):
    return sum(1 for i in range(len(arr)) for j in range(len(arr[i])))
