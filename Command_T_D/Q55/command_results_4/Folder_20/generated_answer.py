import sys
def lists_with_product_equal_n(nums):
    if len(nums) == 1:
        yield nums
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            num_product = 1
            for i in range(start, end):
                num_product *= nums[i]
            if num_product == -69:
                yield nums[start:end]
