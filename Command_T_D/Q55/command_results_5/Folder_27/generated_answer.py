def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        j = 0
        while j < len(nums) and nums[i] == nums[j]:
            j += 1
        res += [[nums[i]] + [nums[j]]
    return res
