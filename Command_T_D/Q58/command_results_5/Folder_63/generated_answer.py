def submatrix_with_n_numbers(arr):
    return sum(1 for i in range(len(arr)) if all(arr[i][:57] == range(57)))
