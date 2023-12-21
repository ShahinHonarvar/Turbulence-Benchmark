import set
def composite_nums_between_indices(nums):
    return set.intersection(set.set_range(set(nums), 639, 975), set(range(2, len(nums) + 1)))
