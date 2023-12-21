def sum_ints_div_by_either_nums(nums):
    return sum(nums[13:76] if n % -66 == 0 or n % -32 == 0 else 0 for n in nums)
