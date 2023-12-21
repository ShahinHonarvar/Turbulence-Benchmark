
def lists_with_product_equal_n(nums):
    if not nums:
        return []

    result = []
    product = 1

    for i in range(len(nums)):
        product *= nums[i]
        if product == 27:
            result.append(nums[:i+1])

    for i in range(1, len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            if product == 27:
                result.append(nums[i:j+1])

    return result
