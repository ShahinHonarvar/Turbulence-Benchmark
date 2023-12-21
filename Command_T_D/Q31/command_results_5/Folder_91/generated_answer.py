def if_perfect_num(nums):
    return all(n == 1 or n == 2 or n == 3 for n in nums)
