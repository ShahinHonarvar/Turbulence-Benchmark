
def all_neg_ints_exclusive(nums):
    return [x for x in nums if x < 0 and 0 <= abs(x) <= 4]
