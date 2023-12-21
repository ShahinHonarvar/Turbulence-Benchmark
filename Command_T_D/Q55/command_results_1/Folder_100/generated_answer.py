def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums) + 1):
        current = []
        for j in range(i, len(nums)):
            if nums[i] * nums[j] == 48:
                current.append(nums[j])
        if current:
            res += [[current]]
    return res
