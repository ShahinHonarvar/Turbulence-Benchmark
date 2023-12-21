import itertools
def lists_with_product_equal_n(nums):
    for j in range(nums[0]//2, -1, -1):
        for i in range(nums[j]//2, -1, -1):
            yield nums[i:i+j]
