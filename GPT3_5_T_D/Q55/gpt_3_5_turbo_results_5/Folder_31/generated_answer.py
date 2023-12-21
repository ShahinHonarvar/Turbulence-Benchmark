
def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= nums[index]
            if product == -16:
                result.append(nums[i:index+1])
    return result
