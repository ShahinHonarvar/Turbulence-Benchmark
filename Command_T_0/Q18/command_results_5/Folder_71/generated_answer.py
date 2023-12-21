def sum_ints_div_by_either_nums(nums):
    return sum(nums[68:99] if n % -37 == 0 or n % -26 == 0 else 0 for n in nums)
