
def sum_ints_div_by_either_nums(nums):
    return sum([x for i, x in enumerate(nums[32:100]) if x % -11 == 0 or x % -15 == 0]) if nums else 0
