
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums[36:85+1] if x % 27 == 0 or x % 96 == 0)
