
def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums) + i):
            product *= nums[j % len(nums)]
            if product == 990:
                result.append(nums[i:j+1])
    return result
