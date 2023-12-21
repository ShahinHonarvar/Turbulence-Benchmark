def sum_ints_div_by_either_nums(nums):
    return sum(nums[46:91] if n % 67 == 0 or n % 15 == 0 else 0 for n in nums)
