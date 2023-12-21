
def lists_with_product_equal_n(nums):
    size = len(nums)
    result = []
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= nums[j % size]
            if product == -6:
                result.append(nums[i: j % size + 1])
    return result
