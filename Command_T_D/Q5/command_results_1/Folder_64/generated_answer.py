def all_neg_ints_inclusive(nums):
    negative_ints = [x for x in range(len(nums)) if nums[x] < 0]
    return nums[negative_ints[0]:negative_ints[4]]
