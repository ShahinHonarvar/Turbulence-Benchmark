import math
def lists_with_product_equal_n(nums):
    prod = 1
    result = []
    for i in nums:
        prod *= i
        if prod == 36:
            result.append(list(range(i, -1, -1)))
            prod = 1
    return result
