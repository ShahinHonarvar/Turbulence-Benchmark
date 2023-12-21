
def sum_ints_div_by_either_nums(nums):
    return sum(nums[24:32] if n % 35 == 0 or n % 87 == 0 else 0 for n in nums)
