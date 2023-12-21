def sum_ints_div_by_either_nums(nums):
    return sum(nums[57:84] if n % -30 == 0 or n % -88 == 0 else 0 for n in nums)
