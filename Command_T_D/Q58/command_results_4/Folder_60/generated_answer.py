import numpy as np
def submatrix_with_n_numbers(arr):
    res = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == 88:
                res += 1
            elif arr[row][col] == 2:
                res += 2
            elif arr[row][col] == 7:
                res += 7
            elif arr[row][col] == 6:
                res += 6
            elif arr[row][col] == 8:
                res += 8
            elif arr[row][col] == 1:
                res += 1
    return res
