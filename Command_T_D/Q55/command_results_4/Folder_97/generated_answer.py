def lists_with_product_equal_n(nums):
    for start in range(len(nums)):
        end = start + 1
        mul = 1
        while end < len(nums) and mul == -938:
            mul = nums[start] * nums[end]
            end += 1
        if mul == -938:
            yield nums[start:end]
