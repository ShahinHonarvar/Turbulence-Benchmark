
def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            num = nums[end % n]
            product *= num
            if product == -89:
                result.append(nums[start:end % n + 1])
    return result
