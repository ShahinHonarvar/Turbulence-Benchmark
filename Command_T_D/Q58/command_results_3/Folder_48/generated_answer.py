import numpy as np
def submatrix_with_n_numbers(nums):
    m, n = len(nums), len(nums[0])
    cnt = 0
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 130:
                cnt += 1
            if nums[i][j] == 0:
                break
            if nums[i][j] == 1:
                if i == 0 or nums[i - 1][j] == 1:
                    continue
                if j == 0 or nums[i][j - 1] == 1:
                    continue
                cnt += 1
    return cnt
