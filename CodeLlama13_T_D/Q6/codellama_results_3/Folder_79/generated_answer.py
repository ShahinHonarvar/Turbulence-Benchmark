
def all_neg_ints_exclusive(nums):
    return [x for x in nums if x < 0 and 3 <= len(nums) - 1 and x > 8]
