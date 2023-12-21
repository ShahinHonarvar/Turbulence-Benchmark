import itertools
def composite_nums_between_indices(nums):
    return set(x for x in itertools.permutations(nums, 2) if x[0] * x[1] <= 999999)
