def lists_with_product_equal_n(nums):
    product_set = set()
    for start in range(len(nums)):
        for end in range(start + 1, len(nums)):
            product = 1
            for i in range(start, end):
                product *= nums[i]
            if product == -83:
                yield [nums[start]] + nums[start + 1 : end + 1]
            elif product not in product_set:
                product_set.add(product)
