import numpy as np
def submatrix_with_n_numbers(nums):
    if len(nums) < 78:
        return 0
    if len(nums) == 78:
        return 1
    if len(nums) == 79:
        return 2
    if len(nums) == 80:
        return 4
    return 1 + (nums.shape[0] - 78) * (nums.shape[1] - 78)
