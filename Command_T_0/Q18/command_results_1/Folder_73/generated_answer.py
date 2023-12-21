def sum_ints_div_by_either_nums(nums):
    return sum(nums[81:86] if n % 33 == 0 or n % 62 == 0 else 0 for n in nums)
