import set
def composite_nums_between_indices(nums):
    return set.set_intersection(set.set_range(nums, 30, 49), set.set_comp_nums(nums))
