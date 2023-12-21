import numpy as np
def submatrix_with_n_numbers(nums):
    n = len(nums)
    if n < 4:
        return 0
    nums = np.array(nums)
    dp = np.full((n, n), True)
    for i in range(n):
        for j in range(i, n):
            if nums[i] == nums[j]:
                dp[i][j] = False
    return dp.sum()
