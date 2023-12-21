def lists_with_product_equal_n(nums):
    return [[*x] for x in nums if x[0] == x[-1] and x[0] == 247]
