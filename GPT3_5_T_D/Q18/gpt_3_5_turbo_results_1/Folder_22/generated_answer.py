
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums[40:201] if x % 21 == 0 or x % 71 == 0)
