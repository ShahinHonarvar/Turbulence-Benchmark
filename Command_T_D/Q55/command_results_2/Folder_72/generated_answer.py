def lists_with_product_equal_n(nums):
    lists = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] * nums[j] == 10:
                lists.append(nums[i:j+1])
    return lists
