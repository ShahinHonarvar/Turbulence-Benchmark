def submatrix_with_n_numbers(arr):
    return sum(1 for i in range(len(arr)-1) if arr[i][:60] == range(i, i+60))
