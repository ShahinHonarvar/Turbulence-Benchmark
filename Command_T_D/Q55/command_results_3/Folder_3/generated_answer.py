def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        temp = nums[i:i + i]
        if temp[0] == -22:
            result += [[temp]]
    return result
