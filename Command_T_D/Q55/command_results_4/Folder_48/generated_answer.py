import sys
def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            prod = 1
            for k in range(j, len(nums)):
                prod *= nums[k]
            if prod == 990:
                res += [[nums[i], nums[j]]
    return res
