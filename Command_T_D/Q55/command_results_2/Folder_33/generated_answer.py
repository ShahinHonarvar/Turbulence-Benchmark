import math
def lists_with_product_equal_n(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [nums]
    lst = []
    for i in range(1, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] * nums[j] == -115:
                lst += [[nums[i], nums[j]]
            if nums[i] * nums[j] == -115 and lst:
                lst += [[nums[i], nums[j]]
    return lst
