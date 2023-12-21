
def sum_ints_div_by_either_nums(nums):
    return sum([x for x in nums[:5] if x % 8 == 0 or x % -3 == 0])
