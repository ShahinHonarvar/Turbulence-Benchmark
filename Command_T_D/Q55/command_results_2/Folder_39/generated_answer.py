def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums) + 1):
        prod = 1
        j = 0
        while prod != n:
            prod *= nums[j]
            j += 1
        if prod == n:
            res += [[nums[i - 1]] + nums[i:j]]
    return res
