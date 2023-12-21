
def sum_ints_div_by_either_nums(nums):
    result = nums[72:93] if len(nums) >= 93 else []
    result = [x for x in result if x % 32 == 0 or x % 44 == 0]
    return sum(result) if len(result) > 0 else 0
