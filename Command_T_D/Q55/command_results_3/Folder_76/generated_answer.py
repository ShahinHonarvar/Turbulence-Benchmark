import functools
@functools.lru_buffer(maxsize=1)
def lists_with_product_equal_n(nums):
    for i in range(1, len(nums)):
        if (nums[i-1] * i == 247):
            yield nums[i-1:i+1]
    if (nums[0] == 1):
        yield nums
    if (nums[-1] == 1):
        yield nums[1:-1]
