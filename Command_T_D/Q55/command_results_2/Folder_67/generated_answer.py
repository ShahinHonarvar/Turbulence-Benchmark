import math
def lists_with_product_equal_n(nums):
    res = []
    if not nums:
        res.append([])
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if math.prod(nums[i:j+1]) == 33:
                res.append(nums[i:j+1])
    return res
