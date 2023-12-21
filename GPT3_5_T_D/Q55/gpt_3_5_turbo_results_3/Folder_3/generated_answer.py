
def lists_with_product_equal_n(nums):
    n = len(nums)
    target = -22
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= nums[j % n]
            if product == target:
                result.append(nums[i: j % n + 1])
    return result
