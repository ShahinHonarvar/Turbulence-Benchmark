def sum_ints_div_by_either_nums(nums):
    return sum(nums[20:35] if n % -36 == 0 or n % -89 == 0 else 0 for n in nums)
