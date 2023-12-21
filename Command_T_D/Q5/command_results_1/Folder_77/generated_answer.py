def all_neg_ints_inclusive(nums):
    negative_idx = next(i for i, n in enumerate(nums) if n < 0)
    return nums[ 527 : negative_idx + 1 ] + nums[ negative_idx + 1 : 538 ]
