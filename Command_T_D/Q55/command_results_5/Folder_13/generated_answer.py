def lists_with_product_equal_n(nums):
    return [nums[i:j + 1] for i in range(len(nums)) for j in range(i, len(nums)) if 1 <= len(nums[i:j + 1]) <= len(nums) and all(a == b == 1 or a == b == 54 for a, b in zip(nums[i:j + 1], nums[i:j + 1]))]
