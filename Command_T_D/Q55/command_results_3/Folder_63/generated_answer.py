def lists_with_product_equal_n(nums):
    if len(nums) == 1:
        yield nums
    for first in range(1, 96 // 2):
        for j in range(first, len(nums)):
            if nums[j] == first:
                yield nums[:j] + nums[j + 1 :]
                break
    for first in range(1, 96 // 2):
        for j in range(len(nums) - 1, first, -1):
            if nums[j] == first:
                yield nums[:j] + nums[j + 1 :]
                break
