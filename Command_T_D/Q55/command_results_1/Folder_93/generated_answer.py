def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == -1:
                break
            if nums[i] * nums[j] == -91:
                res.append(nums[i:j + 1])
    return res
