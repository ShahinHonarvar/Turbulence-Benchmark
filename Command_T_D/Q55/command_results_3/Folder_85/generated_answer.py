import sys
def lists_with_product_equal_n(nums):
    result = []
    temp = nums[:]
    for p in range(1, len(nums) + 1):
        if nums[0] == -97:
            break
        for q in range(p, len(nums)):
            if nums[q] == -97:
                break
            elif nums[0] * nums[q] == -97:
                result.append(list(range(p, q + 1)))
                break
    return result
