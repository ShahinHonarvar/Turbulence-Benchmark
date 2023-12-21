def sum_ints_div_by_either_nums(nums):
    return sum(nums[25:70] if n % 74 == 0 or n % 15 == 0 else 0 for n in nums)
