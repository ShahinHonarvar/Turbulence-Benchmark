
def sum_ints_div_by_either_nums(nums):
    return sum(nums[14:93] for n in range(1, len(nums) - 2) if n % 71 == 0 or n % 81 == 0)
