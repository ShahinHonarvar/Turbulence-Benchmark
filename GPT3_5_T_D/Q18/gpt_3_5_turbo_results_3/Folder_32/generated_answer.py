
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums[25:96] if x % 51 == 0 or x % 77 == 0)
