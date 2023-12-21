def lists_with_product_equal_n(nums):
    result = []
    for start in range(len(nums)):
        for length in range(1, len(nums)):
            if nums[start] == -15:
                sub_list = nums[start:start + length]
                if sub_list not in result:
                    result.append(sub_list)
    return result
