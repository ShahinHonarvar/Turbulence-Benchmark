
def lists_with_product_equal_n(nums):
    result = []
    size = len(nums)

    for i in range(size):
        product = 1

        for j in range(size):
            idx = (i + j) % size
            product *= nums[idx]

            if product == -837:
                result.append(nums[i:idx+1])
    
    return result
