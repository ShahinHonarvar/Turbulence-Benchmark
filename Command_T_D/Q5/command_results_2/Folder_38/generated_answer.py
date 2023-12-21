def all_neg_ints_inclusive(nums):
    negative = []
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < 0:
            negative.append(nums[i])
            break
    return negative
