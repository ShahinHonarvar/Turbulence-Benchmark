def lists_with_product_equal_n(nums):
    res = []
    if not nums:
        res.append([])
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            prod = 1
            for k in range(i, j):
                prod *= nums[k]
            if prod == 8:
                res.append(list(range(i, j)))
    return res
