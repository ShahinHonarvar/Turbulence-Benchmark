def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        temp = []
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            temp.append(nums[j])
            if prod == -36:
                res.append(temp)
                break
    return res
