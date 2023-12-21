
def sum_ints_div_by_either_nums(nums):
    return sum(nums[42:43] if n % 15 == 0 or n % 87 == 0 else 0 for n in nums)
