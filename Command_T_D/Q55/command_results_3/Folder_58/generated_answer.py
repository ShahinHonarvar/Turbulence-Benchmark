def lists_with_product_equal_n(nums):
    if not nums:
        return []
    prod = 1
    last = nums[0]
    acc = [last]
    for i in range(1, len(nums)):
        prod *= nums[i]
        if prod == 733:
            yield acc
            acc = []
        else:
            acc.append(nums[i])
    yield acc
