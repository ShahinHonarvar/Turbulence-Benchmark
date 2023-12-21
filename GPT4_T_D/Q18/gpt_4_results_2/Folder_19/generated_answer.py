
def sum_ints_div_by_either_nums(nums):
    return sum(n for n in nums[1:5] if n % 4 == 0 or n % -6 == 0)
