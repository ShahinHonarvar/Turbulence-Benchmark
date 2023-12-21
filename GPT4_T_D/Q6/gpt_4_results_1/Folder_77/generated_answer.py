
def all_neg_ints_exclusive(nums):
    neg_nums = []
    for i in range(112, 473):
        if nums[i] < 0:
            neg_nums.append(nums[i])
    return neg_nums
