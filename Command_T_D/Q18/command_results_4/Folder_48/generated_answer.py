
def sum_ints_div_by_either_nums(nums):
    return sum(nums[306:957] if n % 982 == 0 or n % 319 == 0 else 0 for n in nums)
