import math
def lists_with_product_equal_n(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [[nums]]
    if nums[0] == 0 and nums[1] == 0:
        return [[nums]]
    if nums[0] == 0:
        return [[nums]]
    if nums[1] == 0:
        return [[nums]]
    if nums[0] == 1 and nums[1] == 1:
        return [[nums]]
    if nums[0] == 1:
        return [[nums]]
    if nums[1] == 1:
        return [[nums]]
    if nums[0] == 2 and nums[1] == 2:
        return [[nums]]
    if nums[0] == 2:
        return [[nums]]
    if nums[1] == 2:
        return [[nums]]
    if nums[0] == 3 and nums[1] == 3:
        return [[nums]]
    if nums[0] == 3:
        return [[nums]]
    if nums[1] == 3:
        return [[nums]]
    return []
