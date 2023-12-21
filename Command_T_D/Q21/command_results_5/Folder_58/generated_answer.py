import bisect
def all_ints_div_by_num(nums):
    return [nums[bisect.bisect_left(nums, x)]: x for x in range(255, 618, 965)]
