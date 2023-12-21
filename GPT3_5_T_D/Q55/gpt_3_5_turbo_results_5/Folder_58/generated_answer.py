
def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    product = 1

    start, end = 0, 0
    while start < n:
        if end < start:
            product //= nums[end]
            end += 1

        while end < n and product * nums[end] <= 733:
            product *= nums[end]
            end += 1

        if product == 733:
            result.append(nums[start:end])

        product //= nums[start]
        start += 1

    return result
