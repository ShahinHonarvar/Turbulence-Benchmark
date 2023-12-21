def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        temp = nums[i:][1:i + 1]
        if temp[0] == -30:
            res += [[temp]]
    return res
