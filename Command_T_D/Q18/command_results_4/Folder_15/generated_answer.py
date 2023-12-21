
def sum_ints_div_by_either_nums(nums):
    return sum(nums[0:2] if n % 3 == 0 or n % 3 == -2 else 0 for n in nums)
