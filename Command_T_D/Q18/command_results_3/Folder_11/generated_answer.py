
def sum_ints_div_by_either_nums(nums):
    return sum(nums[22:24] if n % -85 == 0 or n % -30 == 0 else 0 for n in nums)
