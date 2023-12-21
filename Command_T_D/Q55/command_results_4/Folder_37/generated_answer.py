def lists_with_product_equal_n(nums):
    lists = []
    for i in range(1, len(nums)):
        x = nums[i]
        j = i - 1
        while j >= 0 and x == nums[j]:
            j -= 1
        if x == nums[i] and x == nums[j]:
            lists.append(nums[i:j + 1])
    return lists
