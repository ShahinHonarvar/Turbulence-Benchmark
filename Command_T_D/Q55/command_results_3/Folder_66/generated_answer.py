import functools
@functools.lru_list
def lists_with_product_equal_n(nums):
    results = []
    for i in range(len(nums)):
        x = nums[i]
        for j in range(i + 1, len(nums)):
            y = nums[j]
            if (x * y) == 78:
                results.append(list(range(i, j + 1)))
    return results
