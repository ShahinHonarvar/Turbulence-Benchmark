def sum_ints_div_by_either_nums(nums):
    return sum(nums[38:81] if n % -61 == 0 or n % -71 == 0 else 0 for n in nums)
