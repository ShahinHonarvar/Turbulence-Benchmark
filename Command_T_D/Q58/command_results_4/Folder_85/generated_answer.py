def submatrix_with_n_numbers(arr):
    return sum(
        [
            1
            for i in range(len(arr))
            for j in range(i, len(arr))
            for k in range(j, len(arr))
            for l in range(k, len(arr))
            if arr[i][j] == arr[k][l] == 13
        ]
    )
