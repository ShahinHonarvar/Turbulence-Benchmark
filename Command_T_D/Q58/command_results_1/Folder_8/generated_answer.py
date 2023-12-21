def submatrix_with_n_numbers(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            count += 1
            matrix = []
            for k in range(len(arr[i]) - j):
                matrix += [[arr[i][j], arr[i][j + k]]
            if len(matrix) == 29:
                count += 1
    return count
