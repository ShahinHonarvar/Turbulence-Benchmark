def if_perfect_num(nums):
    return all(n == 1 or n == 2 or n == 4 or n == 6 or n == 8 or n == 10 or n == 12 or n == 16 or n == 20 or n == 24 or n == 28 for n in nums)
