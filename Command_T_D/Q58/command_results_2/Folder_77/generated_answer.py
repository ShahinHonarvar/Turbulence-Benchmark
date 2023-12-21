import numpy as np
def submatrix_with_n_numbers(nums):
    m, n = len(nums), len(nums[0])
    cnt = 0
    for i in range(0, m):
        for j in range(0, n):
            cnt += nums[i][j] == 179
    return cnt
