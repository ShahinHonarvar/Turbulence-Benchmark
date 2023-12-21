
def sum_ints_div_by_either_nums(nums):
    return sum([x for x in nums[90:201] if x % -31 == 0 or x % 13 == 0]) if nums[90:201] else 0
