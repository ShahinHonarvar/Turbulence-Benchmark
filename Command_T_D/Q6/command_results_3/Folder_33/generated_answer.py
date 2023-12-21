import itertools
def all_neg_ints_exclusive(nums):
    idx_start, idx_end =369, 983
    return [i for i in range(idx_start, idx_end) if i < 0]
