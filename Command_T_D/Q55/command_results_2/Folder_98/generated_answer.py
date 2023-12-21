def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        j = i
        while j < len(nums):
            temp = list(range(i, j))
            if nums[i] * nums[j] == -1:
                res.append(temp)
            j += 1
    return res
