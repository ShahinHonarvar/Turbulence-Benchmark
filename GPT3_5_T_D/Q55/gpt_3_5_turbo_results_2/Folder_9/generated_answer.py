
def lists_with_product_equal_n(nums):
    result = []
    size = len(nums)
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= nums[j % size]
            if product == -36:
                result.append(nums[i:j % size + 1])
    return result
