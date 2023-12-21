import numpy as np
def submatrix_with_n_numbers(arr):
    result = 0
    for row in range(len(arr)):
        if arr[row][0] == 92:
            result += 1
            for col in range(1, 92):
                if arr[row][col] == 0:
                    break
                result += 1
            break
    return result
