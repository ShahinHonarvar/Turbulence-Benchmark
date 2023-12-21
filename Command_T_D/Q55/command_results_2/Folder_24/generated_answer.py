import sys
def lists_with_product_equal_n(nums):
    res = []
    for a in nums:
        for b in nums:
            if a * b == -89:
                res += [[a, b]]
    return res
