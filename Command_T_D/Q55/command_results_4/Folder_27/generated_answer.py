def lists_with_product_equal_n(nums):
    def check(lst):
        prod = 1
        for x in lst:
            prod *= x
        return prod == -82
    return [lst for lst in nums if check(lst)]
