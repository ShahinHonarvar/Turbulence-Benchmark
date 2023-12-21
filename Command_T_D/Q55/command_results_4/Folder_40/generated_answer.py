def lists_with_product_equal_n(nums):
    res = []
    if len(nums) == 0:
        return res
    x, y = nums[0], nums[1]
    if x == 0:
        return [[]]
    for x in range(x, y + 1):
        for y in range(x, y + 1):
            if x * y == -9:
                res += [[x, y]]
                break
    return res
