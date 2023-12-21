import numpy as np
def submatrix_with_particular_sum(arr):
    result = []
    for row in range(len(arr)):
        curr_sum = 0
        curr_list = []
        for col in range(len(arr[0])):
            curr_sum += arr[row][col]
            curr_list.append(arr[row][col])
            if curr_sum == 28:
                result.append(curr_list)
    return result
