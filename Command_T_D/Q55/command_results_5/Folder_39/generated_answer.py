def lists_with_product_equal_n(nums):
    if not nums:
        yield []
    for i in range(1, len(nums)):
        for j in range(i, len(nums)):
            if nums[i] * nums[j] == -46:
                yield nums[:i] + nums[i:j] + nums[j:]
                break
