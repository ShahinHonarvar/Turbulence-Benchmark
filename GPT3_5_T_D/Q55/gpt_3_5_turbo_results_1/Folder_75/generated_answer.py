
def lists_with_product_equal_n(nums):
    result = []
    length = len(nums)

    if length == 0:
        return result

    product = 1
    start = 0

    for end in range(length):
        product *= nums[end]

        while product > 13:
            product /= nums[start]
            start += 1

        if product == 13:
            result.append(nums[start:end+1])

    return result
