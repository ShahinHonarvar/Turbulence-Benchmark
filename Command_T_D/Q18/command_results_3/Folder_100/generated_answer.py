
def sum_ints_div_by_either_nums(nums):
    return sum(nums[72:93] if n % 32 == 0 or n % 44 == 0 else 0 for n in nums)
