
def sum_ints_div_by_either_nums(nums):
    return sum(nums[0:2] if n % 2 == 0 or n % 2 == 1 else 0 for n in nums)
