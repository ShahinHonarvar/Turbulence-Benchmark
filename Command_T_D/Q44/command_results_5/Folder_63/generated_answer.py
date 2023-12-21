import set
def composite_nums_between_indices(nums):
    return set.set_intersection(set.set_complement(set(range(17, 79)), nums), nums)
