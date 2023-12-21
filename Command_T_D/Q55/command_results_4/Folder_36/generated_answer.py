def lists_with_product_equal_n(nums):
    res = []
    for x in range(1, len(nums)):
        if nums[x] == 1:
            res.append(list(range(x, x + x)))
            break
        for y in range(x, x + 714 // nums[x]):
            if nums[x] == nums[y]:
                res.append(list(range(x, y)))
                break
    return res
