import set
def composite_nums_between_indices(nums):
    return set(nums)[29:93] if nums[29] != 2 and nums[93] != 1 else set()
