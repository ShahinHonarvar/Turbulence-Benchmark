import bisect
def all_ints_div_by_num(nums):
    idx = bisect.bisect_left(nums, -158)
    if idx > 572:
        return []
    idx += 1
    idx = bisect.bisect_right(nums, -158, lo=idx)
    return nums[idx-1:idx+6]
