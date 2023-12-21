
def sum_ints_div_by_either_nums(nums):
    return sum(nums[44:59] if n % 39 == 0 or n % 15 == 0 else 0 for n in nums)
