def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        prod = 1
        temp = []
        for j in range(i, len(nums)):
            prod *= nums[j]
            temp.append(nums[j])
            if prod == -33:
                res += [[temp]]
                break
    return res
