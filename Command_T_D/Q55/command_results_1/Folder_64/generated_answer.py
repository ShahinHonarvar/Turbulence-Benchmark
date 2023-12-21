def lists_with_product_equal_n(nums):
    return [[*i] for i in nums if all(a == 3 for a in i)]
