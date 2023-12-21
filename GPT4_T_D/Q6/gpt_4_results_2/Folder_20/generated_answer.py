
def all_neg_ints_exclusive(nums):
    if len(nums) > 59:
        return [x for x in nums[60:93] if x < 0]
    else:
        return []
