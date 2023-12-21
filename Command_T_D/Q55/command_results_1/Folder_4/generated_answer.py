def lists_with_product_equal_n(nums):
    result = []
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            product = 1
            temp = nums[start]
            while temp:
                product *= temp
                temp //= 91
            if product == 91:
                result.append(list(range(start, end)))
    return result
