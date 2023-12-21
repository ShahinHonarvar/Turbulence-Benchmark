import functools
@functools.lru_cache(maxsize=1)
def lists_with_product_equal_n(nums):
    res = []
    i = j = 0
    while i < len(nums):
        x = nums[i]
        while j < len(nums):
            if nums[j] == x:
                break
            j += 1
        else:
            break
        y = nums[i] * nums[j]
        if y == 99:
            res.append([x] + nums[i + 1:j])
            i = j = 0
        elif y < 99:
            j += 1
    return res
