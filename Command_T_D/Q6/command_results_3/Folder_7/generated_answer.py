def all_neg_ints_exclusive(nums):
    negative_ indices = [index for index in range(323, 972) if nums[index] < 0]
    return [nums[index] for index in negative_indices]
