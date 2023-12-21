
def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    product = 1
    start = 0
    for end in range(n + 1):
        while product < -906 and start < end:
            product /= nums[start]
            start += 1
        if product == -906:
            result.append(nums[start:end])
        if end < n:
            product *= nums[end]
    return result
