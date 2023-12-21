def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        j = i + 1
        while j < len(nums) and nums[i] * nums[j] == 74:
            j += 1
        res.append(list(range(i, j - 1)))
    return res
