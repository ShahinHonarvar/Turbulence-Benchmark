def lists_with_product_equal_n(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [[]]
    if nums[0] == 1:
        return [[nums[0]]]
    result = []
    for i in range(1, len(nums)):
        if nums[i] == 1:
            continue
        temp = []
        for j in range(i, len(nums)):
            if nums[j] == 1:
                break
            temp.append(nums[j])
        result.append(temp)
    return result
