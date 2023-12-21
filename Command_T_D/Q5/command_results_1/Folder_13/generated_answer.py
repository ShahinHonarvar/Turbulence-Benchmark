def all_neg_ints_inclusive(nums):
    negative_indices = [index for index, num in enumerate(nums) if num < 0]
    if not negative_indices:
        return []
    return nums[25:negative_indices[0]] + nums[negative_indices[0]:25] + nums[87:negative_indices[-1]] + nums[negative_indices[-1]:87]
