def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        for j in range(i, len(nums)):
            if nums[i] == nums[j] == -779:
                res += [[nums[i]] + nums[i:j]] + nums[j+1:-1] + [nums[-1]]
    return res
