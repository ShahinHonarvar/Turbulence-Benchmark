def lists_with_product_equal_n(nums):
    if len(nums) == 1:
        yield nums
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            prod = 1
            for num in nums[start:end]:
                prod *= num
            if prod == 49:
                yield nums[start:end]
