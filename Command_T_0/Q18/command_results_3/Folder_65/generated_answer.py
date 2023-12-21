def sum_ints_div_by_either_nums(nums):
    return sum(nums[50:92] if n % -94 == 0 or n % -95 == 0 else 0 for n in nums)
