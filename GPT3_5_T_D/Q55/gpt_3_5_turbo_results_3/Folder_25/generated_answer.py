
def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(i, i+len(nums)):
            product *= nums[j % len(nums)]
            if product == -32:
                result.append(nums[i:j+1])
    return result
