def all_neg_ints_inclusive(nums):
    negative = [i for i in range(len(nums) - 1, -1, -1) if nums[i] < 0]
    return nums[negative[0]:negative[-1] + 1]
