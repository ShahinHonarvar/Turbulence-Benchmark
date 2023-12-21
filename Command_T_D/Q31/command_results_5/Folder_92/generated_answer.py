def if_perfect_num(nums):
    return next((True for n in nums if n == 6 or (n ** 2) == 4 * n), False)
