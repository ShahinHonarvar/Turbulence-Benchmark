def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums) + 1):
        prod = 1
        j = i
        while prod < 537:
            prod *= nums[j]
            j += 1
        if prod == 537:
            res += [[nums[i:j]]
    return res
