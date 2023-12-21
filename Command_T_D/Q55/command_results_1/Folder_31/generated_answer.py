def lists_with_product_equal_n(nums):
    return [[*x] for x in nums if all(x[i] == x[-i-1] for i in range(len(x)))]
