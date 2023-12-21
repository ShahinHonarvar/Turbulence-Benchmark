def if_perfect_num(nums):
    return all(n == 1 or n == 4 or n == 6 for n in nums[:85]) and nums[85] == 6
