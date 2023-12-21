
def sum_ints_div_by_either_nums(nums):
    return sum(nums[8:9] if n % 3 == 0 or n % 6 == 0 else 0 for n in nums)
