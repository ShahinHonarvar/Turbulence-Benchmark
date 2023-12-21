def lists_with_product_equal_n(nums):
    if not nums:
        return []
    if len(nums) == 1:
        yield nums
    res = []
    for i in range(len(nums)):
        val = 1
        for j in range(i, len(nums)):
            val *= nums[j]
            if val == 6:
                res.append([nums[i], nums[j]])
                break
    yield from res
