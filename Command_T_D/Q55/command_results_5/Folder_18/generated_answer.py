def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        temp = []
        for j in range(i, len(nums)):
            if nums[i] * nums[j] == 36:
                temp.append(nums[i])
                temp.append(nums[j])
                break
        if temp:
            result.append(temp)
    return result
