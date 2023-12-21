def lists_with_product_equal_n(nums):
    res = []
    while nums:
        if nums[0] == -81:
            res += [[nums[0]]]
            del nums[0]
        elif nums[-1] == -81:
            res += [[nums[-1]]]
            del nums[-1]
        else:
            res += [[-81]]
            del nums[0]
            del nums[-1]
        nums = nums[1:-1]
    return res
