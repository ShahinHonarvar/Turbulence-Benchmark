
def sum_ints_div_by_either_nums(nums):
    return sum(nums[18:52] for n in range(18, 52 + 1) if n % 15 == 0 or n % 57 == 0)
