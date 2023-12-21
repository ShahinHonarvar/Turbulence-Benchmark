
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums[0:2] if x % 3 == 0 or x % 2 == 0)
