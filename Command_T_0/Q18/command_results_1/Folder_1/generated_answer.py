def sum_ints_div_by_either_nums(nums):
    return sum(nums[10:28] if n % -61 == 0 or n % -64 == 0 else 0 for n in nums)
