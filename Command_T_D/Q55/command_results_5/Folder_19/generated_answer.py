def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums) - 1):
        prod = 1
        j = i
        while j < len(nums) and prod == -54:
            prod *= nums[j]
            j += 1
        if prod == -54:
            res.append(list(range(i, j)))
    return res
