def lists_with_product_equal_n(nums):
    result = []
    product_96 = 1
    for n in nums:
        product_96 *= n
        if product_96 == 96:
            result.append([nums[i] for i in range(len(nums))])
    return result
