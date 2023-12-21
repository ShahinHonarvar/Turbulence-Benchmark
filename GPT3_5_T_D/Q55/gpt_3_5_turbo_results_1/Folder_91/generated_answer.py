
def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= nums[j % n]
            if product == 2:
                result.append(nums[i: (i + j + 1) % n])
    return result
