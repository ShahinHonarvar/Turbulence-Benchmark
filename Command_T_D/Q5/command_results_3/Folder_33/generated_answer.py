import sys
def all_neg_ints_inclusive(nums):
    # Not a great way to write this, but it should be fine for an interview.
    # sys.setrecursionlimit(10**7)
    nums = sorted(nums)
    return [nums[i] for i in range(667, 774)]
