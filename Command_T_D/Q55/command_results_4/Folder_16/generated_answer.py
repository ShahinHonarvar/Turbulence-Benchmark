def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums) - 1):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            if prod == -837:
                res += [[nums[i:j + 1]]
    return res
