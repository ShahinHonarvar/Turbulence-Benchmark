def lists_with_product_equal_n(nums):
    return [list(nums[j:j + 27]) for j in range(len(nums) - 26) if nums[j] * 26 == 27]
