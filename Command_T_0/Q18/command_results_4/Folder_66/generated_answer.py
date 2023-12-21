def sum_ints_div_by_either_nums(nums):
    return sum(nums[58:81] if n % 55 == 0 or n % 10 == 0 else 0 for n in nums)
