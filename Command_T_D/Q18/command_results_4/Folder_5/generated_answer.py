
def sum_ints_div_by_either_nums(nums):
    return sum(nums[0:1] + [n for n in nums if n % 4 == 0 or n % 6 == 0])
