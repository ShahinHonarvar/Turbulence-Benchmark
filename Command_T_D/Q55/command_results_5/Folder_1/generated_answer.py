def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        j = nums[i]
        while i != j:
            if nums[i] * nums[j] == -51:
                res += [[nums[i], nums[j]]
            i += 1
            j += 1
    return res
