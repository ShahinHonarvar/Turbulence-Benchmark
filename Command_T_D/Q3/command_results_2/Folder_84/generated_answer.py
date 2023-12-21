def all_pos_ints_inclusive(nums):
    result = [nums[43:86] for i in range(nums.count(0)) if nums[i] > 0]
    return result if len(result) else []
