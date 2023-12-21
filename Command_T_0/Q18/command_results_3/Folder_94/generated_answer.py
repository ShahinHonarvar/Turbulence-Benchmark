def sum_ints_div_by_either_nums(nums):
    return sum(nums[93:94] if n % -53 == 0 or n % -91 == 0 else 0 for n in nums)
