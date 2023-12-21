import numpy as np
def submatrix_with_n_numbers(nums):
    res = 0
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j] == 1:
                res += 1
            else:
                break
    return res
