def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums) - 1):
        x = nums[i]
        j = i
        while True:
            if nums[j] == x:
                break
            elif nums[j] == 1:
                return res
            j += 1
            x *= nums[j]
            if x == 990:
                res.append([x])
                break
    return res
