
def lists_with_product_equal_n(nums):
    if len(nums) == 0:
        return []

    result = []
    product = 1

    for i in range(len(nums)):
        product *= nums[i]

        if product == -26:
            result.append(nums[:i+1])

        for j in range(i+1, len(nums)):
            product *= nums[j]

            if product == -26:
                result.append(nums[i+1:j+1])

    return result
