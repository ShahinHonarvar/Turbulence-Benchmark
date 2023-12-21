def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        temp = []
        x = nums[i]
        while temp:
            temp.append(nums[i])
            if temp[-1] == x:
                break
            x *= temp[-1]
            temp.append(nums[i])
            res += [[x]]
    return res
