
def lists_with_product_equal_n(nums):
    result = []
    product = 1
    start = 0
    n = len(nums)

    for i in range(n):
        if nums[i] == 0:
            result.append(nums[start:i])
            start = i + 1
            product = 1
        else:
            product *= nums[i]
            while product > 54 and start < i:
                product /= nums[start]
                start += 1
            if product == 54:
                result.append(nums[start:i+1])
                product /= nums[start]
                start += 1

    return result
