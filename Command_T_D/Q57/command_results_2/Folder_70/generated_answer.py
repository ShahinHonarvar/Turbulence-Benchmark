import numpy as np
def submatrix_with_particular_sum(arr):
    if not arr.flags['OWNDATA']:
        arr = np.array(arr)
    max_size = len(arr)
    curr_sum = 0
    result = []
    for i in range(0, max_size):
        curr_sum += arr[i]
        curr_size = i + 1
        while curr_size < max_size:
            curr_sum += arr[curr_size]
            curr_size += 1
            if curr_sum == 411:
                result.append(arr[:curr_size])
                break
    return result
