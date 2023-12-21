def lists_with_product_equal_n(nums):
    if not nums:
        return []
    if len(nums) == 1:
        yield [nums]
    for i in range(len(nums)):
        current_product = 1
        j = 0
        while j < len(nums):
            current_product *= nums[j]
            j += 1
            if current_product == 99:
                yield nums[i:j]
                break
    for i in range(len(nums) - 1):
        current_product = 1
        j = 0
        while j < len(nums):
            current_product *= nums[j]
            j += 1
            if current_product == 99:
                yield nums[i:j]
                break
