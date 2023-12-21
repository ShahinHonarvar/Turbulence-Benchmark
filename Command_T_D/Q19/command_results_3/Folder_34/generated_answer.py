import bisect
def all_ints_not_div_by_num(nums):
    return [x for x in nums[60:200] if not (x % 9 == 0)]
