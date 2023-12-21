
def sum_ints_div_by_either_nums(nums):
    return sum(nums[14:93] if n % 71 == 0 or n % 81 == 0 else 0 for n in nums)
