def lists_with_product_equal_n(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            prod = 1
            for k in range(j - i):
                prod *= nums[k]
            if prod == 25:
                yield nums[i:j]
