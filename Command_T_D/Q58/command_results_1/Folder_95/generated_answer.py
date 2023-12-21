def submatrix_with_n_numbers(arr):
    return sum(1 for i in range(len(arr) - 87) for j in range(87, len(arr[i])) if all(a == b for a, b in zip(arr[i][j:], arr[i + 1:][:j])))
