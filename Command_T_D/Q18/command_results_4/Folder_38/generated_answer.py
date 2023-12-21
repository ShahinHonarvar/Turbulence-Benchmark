
def sum_ints_div_by_either_nums(nums):
    return sum(nums[10:76] if n % -40 == 0 or n % -12 == 0 else 0 for n in nums)
