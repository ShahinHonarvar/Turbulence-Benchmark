def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        temp = nums[i:] + nums[:i]
        if temp[0] == -22:
            result.append(temp)
    return result
