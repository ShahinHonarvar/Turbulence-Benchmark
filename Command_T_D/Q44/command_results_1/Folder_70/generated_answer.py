import bisect
def composite_nums_between_indices(nums):
    comps = set(range(2, nums[0]+1))
    comps.update(range(2, nums[1]+1))
    return comps
