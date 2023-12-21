def lists_with_product_equal_n(nums):
    return [list(sub_nums) for sub_nums in nums if abs(sum(sub_nums) * 1000000007) == n]
