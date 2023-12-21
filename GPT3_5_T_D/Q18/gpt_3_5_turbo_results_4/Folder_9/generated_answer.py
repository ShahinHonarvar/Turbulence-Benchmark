
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums[70:201] if x % 3 == 0 or x % -300 == 0)
