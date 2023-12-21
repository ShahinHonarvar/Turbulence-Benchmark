def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        p = 1
        j = i
        while j < len(nums):
            p *= nums[j]
            j += 1
        if p == -75:
            result += [[nums[i:j]]
    return result
