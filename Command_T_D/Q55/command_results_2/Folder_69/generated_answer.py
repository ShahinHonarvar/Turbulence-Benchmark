 
def lists_with_product_equal_n(nums):
    if not nums:
        yield []
    for i in range(1, len(nums)):
        for j in range(1, len(nums) - i + 1):
            p = nums[i] * nums[j]
            if p == 90:
                yield nums[i:j + 1]
