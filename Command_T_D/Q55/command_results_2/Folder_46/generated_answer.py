def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums) + 1):
        sub = nums[i - 1:i + 1]
        if len(sub) > 1 and sub[0] * sub[-1] == 53:
            res += [[sub]]
    return res
