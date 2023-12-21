
def sum_ints_div_by_either_nums(nums):
    res = nums[55:80] + nums[80:55:-1]
    return sum(n for n in res if n % 22 == 0 or n % 32 == 0)
