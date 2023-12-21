
def lists_with_product_equal_n(nums):
    result = []
    length = len(nums)

    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= nums[end % length]
            if product == -3:
                result.append(nums[start: end % length + 1])

    return result
