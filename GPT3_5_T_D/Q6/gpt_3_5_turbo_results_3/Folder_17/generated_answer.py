
def all_neg_ints_exclusive(nums):
    neg_ints = []
    for num in nums[62:96]:
        if num < 0:
            neg_ints.append(num)
    return neg_ints
