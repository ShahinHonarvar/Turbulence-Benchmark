def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] * nums[j] == 714:
                res.append(list(range(i, j + 1)))
    return res
