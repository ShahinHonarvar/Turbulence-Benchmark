
def sum_ints_div_by_either_nums(nums):
    return sum(nums[69:97] if n % 90 == 0 or n % 67 == 0 else 0 for n in nums)
