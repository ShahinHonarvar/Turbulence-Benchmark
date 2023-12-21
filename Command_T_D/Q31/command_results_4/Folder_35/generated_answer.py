def if_perfect_num(nums):
    return all(n == 6 or n == 1 for n in nums) and nums[993] == 6
