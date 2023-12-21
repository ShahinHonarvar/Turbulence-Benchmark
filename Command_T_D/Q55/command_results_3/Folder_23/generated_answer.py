def lists_with_product_equal_n(nums):
    result = []
    current_product = 1
    for num in nums:
        current_product = current_product * num
        if current_product == -95:
            result.append(nums[:])
            break
        if current_product == -90:
            result.append(nums[1:])
            break
    return result
