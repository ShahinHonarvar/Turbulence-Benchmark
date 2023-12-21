
def lists_with_product_equal_n(nums):
    n = len(nums)
    product = 1
    result = []
    for i in range(n):
        for j in range(i, n+i):
            product *= nums[j % n]
            if product == 36:
                result.append(nums[i:j % n + 1])
    return result
