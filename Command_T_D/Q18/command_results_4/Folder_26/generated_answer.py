
def sum_ints_div_by_either_nums(nums):
    return sum(nums[69:70] if n % 72 == 0 or n % 70 == 0 else 0 for n in nums)
