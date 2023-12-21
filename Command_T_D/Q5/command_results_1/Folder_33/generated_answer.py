def all_neg_ints_inclusive(nums):
    neg_nums = []
    for i in range(667, 774+1):
        if nums[i] < 0:
            neg_nums.append(nums[i])
    return neg_nums
