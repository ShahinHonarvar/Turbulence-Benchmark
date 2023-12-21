def if_perfect_num(nums):
    return all(n in nums for n in range(1, 85)) and nums[84] == 648
