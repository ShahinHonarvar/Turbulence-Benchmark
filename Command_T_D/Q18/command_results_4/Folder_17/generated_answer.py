
def sum_ints_div_by_either_nums(nums):
    return sum(nums[81:89] if n % 56 == 0 or n % 68 == 0 else 0 for n in nums)
