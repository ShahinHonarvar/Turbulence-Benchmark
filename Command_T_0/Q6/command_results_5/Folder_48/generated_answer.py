def all_neg_ints_exclusive(nums):
    return [x for x in range( 385, 1000 ) if x < 0 and x not in nums]
