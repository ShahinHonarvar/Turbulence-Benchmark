
def lists_with_product_equal_n(nums):
    result = []
    size = len(nums)
    for i in range(size):
        product = 1
        for j in range(size):
            num = nums[(i + j) % size]
            product *= num
            if product == -690:
                result.append(nums[i:i+j+1])
    return result
