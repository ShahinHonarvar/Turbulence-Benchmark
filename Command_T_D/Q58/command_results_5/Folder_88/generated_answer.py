def submatrix_with_n_numbers(arr):
    return sum(1 for i in range(len(arr)) for j in range(i, len(arr)) if len(set(arr[i:j])) == 67)
