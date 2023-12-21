import itertools
def lists_with_product_equal_n(nums):
    if not nums:
        yield []
    for j in range(1, max(nums)):
        for i in range(1, j + 1):
            if nums[i] * nums[j] == 4:
                yield [nums[i]] + list(nums[i+1:j]) + [nums[j]]
                yield [nums[j]] + list(nums[i:j+1])
