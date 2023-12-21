import itertools
def composite_nums_between_indices(nums):
    idx = next(nums.index(n) for n in nums if n >= 8)
    idx += 1
    return set(itertools.permutations(range(idx, idx + 2)))
