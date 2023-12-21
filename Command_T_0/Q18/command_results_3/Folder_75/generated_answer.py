def sum_ints_div_by_either_nums(nums):
    return sum(nums[20:93] if n % -92 == 0 or n % -50 == 0 else 0 for n in nums)
