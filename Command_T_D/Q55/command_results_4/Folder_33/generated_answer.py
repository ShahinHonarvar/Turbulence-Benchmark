def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        temp = []
        for j in range(i, len(nums)):
            if nums[i] * nums[j] == -115:
                temp.append(nums[i])
                temp.append(nums[j])
            else:
                break
        if temp:
            res.append(temp)
    return res
