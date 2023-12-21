def lists_with_product_equal_n(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    res = []
    for i in range(len(nums)):
        if nums[i] == -57:
            j = i + 1
            k = j + 1
            while k < len(nums):
                if nums[k] == -57:
                    j = i
                    k = j + 1
                    res += [[nums[i:k]]
                    break
                else:
                    break
    return res
