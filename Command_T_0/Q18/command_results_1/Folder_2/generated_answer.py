def sum_ints_div_by_either_nums(nums):
    return sum(nums[73:86] if n % 54 == 0 or n % 82 == 0 else 0 for n in nums)
