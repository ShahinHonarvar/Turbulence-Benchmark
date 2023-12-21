
def sum_ints_div_by_either_nums(nums):
    return sum(nums[2:7] if n % -1 == 0 or n % -7 == 0 else 0 for n in nums)
