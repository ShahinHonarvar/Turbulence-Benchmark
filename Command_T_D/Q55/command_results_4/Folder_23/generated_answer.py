def lists_with_product_equal_n(nums):
    res = []
    for x in range(1, nums[0] + 1):
        for i in range(nums[0], len(nums) - 1):
            if nums[i] == x:
                res.append(nums[i:j])
                break
            else:
                res.append(nums[:i] + nums[i:j] + nums[j:])
                break
    return res
