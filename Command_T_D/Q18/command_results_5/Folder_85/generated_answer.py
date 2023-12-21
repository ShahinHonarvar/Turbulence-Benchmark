
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums[1:8] if x % -9 == 0 or x % -3 == 0)
