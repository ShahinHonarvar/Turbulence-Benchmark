
def lists_with_product_equal_n(nums):
    if len(nums) < 1:
        return []
    result = []
    for i in range(len(nums)):
        product = nums[i]
        if product == 47:
            result.append([product])
        for j in range(i+1, len(nums)):
            product *= nums[j]
            if product > 47:
                break
            if product == 47:
                result.append(nums[i:j+1])
    return result
