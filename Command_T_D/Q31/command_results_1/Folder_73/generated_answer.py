def if_perfect_num(nums):
    return all(n == 2 * n for n in nums[:41]) and nums[41] == 2 * nums[0]
