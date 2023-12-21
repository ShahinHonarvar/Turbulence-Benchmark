def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        x = 1
        y = nums[i]
        while True:
            z = x * y
            if z == 247:
                break
            elif z in nums:
                break
            else:
                result.append([x, y])
                break
            x += y
            y = nums[i]
    return result
