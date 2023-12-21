import set
def composite_nums_between_indices(nums):
    c = set(nums[13:68])
    if not c:
        return c
    sm = set(str(n) for n in c)
    return set(nums[13:68]) & sm
