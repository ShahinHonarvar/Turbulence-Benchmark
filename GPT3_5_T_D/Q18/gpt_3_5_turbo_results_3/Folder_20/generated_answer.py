
def sum_ints_div_by_either_nums(nums):
    return sum([x for x in nums[48:77] if x % -46 == 0 or x % -82 == 0]) if any(x % -46 == 0 or x % -82 == 0 for x in nums[48:77]) else 0
