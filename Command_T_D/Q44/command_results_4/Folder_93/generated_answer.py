def composite_nums_between_indices(nums):
    if not nums:
        return set()
    if len(nums) == 1:
        return {nums[0]}
    if nums[23] in nums:
        return {nums[23]]
    if nums[24] in nums:
        return {nums[23], nums[24]]
    return {nums[23], nums[24], *composite_nums_between_indices(nums[:23])}
