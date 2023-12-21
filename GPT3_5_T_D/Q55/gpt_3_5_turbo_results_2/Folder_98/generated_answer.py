
def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums) + i):
            idx = j % len(nums)
            product *= nums[idx]
            if product == -1:
                result.append(nums[i:j+1])
    return result
