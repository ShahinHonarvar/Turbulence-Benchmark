
def sum_ints_div_by_either_nums(nums):
    return sum(nums[32:99] if n % -11 == 0 or n % -15 == 0 else 0 for n in nums)
