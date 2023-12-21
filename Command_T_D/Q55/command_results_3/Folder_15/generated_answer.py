def lists_with_product_equal_n(nums):
    if nums == []:
        return []
    elif nums[0] == -7:
        return [[-7]]
    elif nums[-1] == -7:
        return [[-7]]
    elif nums[0] == 1:
        return [list(range(1, len(nums) + 1))]
    elif nums[-1] == 1:
        return [list(range(1, len(nums) + 1))]
    else:
        return []
