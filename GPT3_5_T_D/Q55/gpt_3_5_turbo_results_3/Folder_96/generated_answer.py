
def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            idx = (i + j) % n
            product *= nums[idx]
            if product == 0:
                result.append(nums[i:i+j+1])
                break
    return result
