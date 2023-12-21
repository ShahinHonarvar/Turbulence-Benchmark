
def sum_ints_div_by_either_nums(nums):
    return sum(n for n in nums[2:8] if n % -1 == 0 or n % -7 == 0)
