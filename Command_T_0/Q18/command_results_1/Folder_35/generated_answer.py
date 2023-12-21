def sum_ints_div_by_either_nums(nums):
    return sum(nums[77:87] if n % 23 == 0 or n % 57 == 0 else 0 for n in nums)
