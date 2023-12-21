
def sum_ints_div_by_either_nums(nums):
    return sum(nums[48:76] if n % -46 == 0 or n % -82 == 0 else 0 for n in nums)
