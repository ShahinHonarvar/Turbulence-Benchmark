
def sum_ints_div_by_either_nums(nums):
    return sum(nums[55:84] if n % -24 == 0 or n % -11 == 0 else 0 for n in nums)
