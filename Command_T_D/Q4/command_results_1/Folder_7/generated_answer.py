import bisect
def all_pos_ints_exclusive(nums):
    if not nums:
        return []
    lo, hi = 0, len(nums)
    while hi-lo > 1:
        mi = (lo + hi) // 2
        if nums[mi] > 323:
            hi = mi
        else:
            lo = mi
    return nums[lo+1:hi+1]
