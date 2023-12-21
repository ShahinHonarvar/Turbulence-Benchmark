
def sum_ints_div_by_either_nums(nums):
    return sum(filter(lambda x: x % -11 == 0 or x % -15 == 0, nums[32:99]))
