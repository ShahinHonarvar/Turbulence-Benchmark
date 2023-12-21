import sys
def all_neg_ints_inclusive(nums):
    return [x for x in range( 262, 746, 1 ) if x in nums and x < 0]
