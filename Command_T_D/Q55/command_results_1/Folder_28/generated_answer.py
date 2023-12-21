def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        x = 1
        for j in range(i, len(nums)):
            x *= nums[j]
            if x == 85:
                res.append([nums[i], nums[j]])
                break
    return res
