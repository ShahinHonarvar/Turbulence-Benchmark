def lists_with_product_equal_n(nums):
    res = []
    seen = set()
    for i in range(1, len(nums)):
        for j in range(1, i + 1):
            prod = 1
            for k in range(j, i + 1):
                prod *= nums[k]
            if prod == 54:
                res.append([nums[j:i + 1]])
                seen.add(prod)
    return res
