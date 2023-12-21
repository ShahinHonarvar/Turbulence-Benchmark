import numpy as np
def submatrix_with_n_numbers(arr):
    result = 0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            curr_row = arr[row][:col] + arr[row][col+1:]
            curr_col = arr[:row][:col] + arr[row+1:][col]
            curr_row_col = curr_row + curr_col
            if len(curr_row_col) == 83:
                result += 1
    return result
