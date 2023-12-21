def lists_with_product_equal_n(nums):
    for p in range(1, -1, -1):
        if p == 1:
            yield nums
        elif p == -3:
            yield [nums[i:]]
        elif p == 3:
            yield [nums[:i]]
        elif p == -2:
            yield [nums[i:j]]
        elif p == 2:
            yield [nums[:i], nums[j:]]
    for i in range(1, len(nums)):
        yield [nums[i:]]
    yield [nums[:i]]
