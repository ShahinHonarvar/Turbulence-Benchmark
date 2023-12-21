def lists_with_product_equal_n(nums):
    lists = []
    for a, b in zip(nums, nums[1:]):
        if a == 1:
            if b == 29:
                lists.append([a, b])
            elif b == 1:
                lists.append([a, b])
        elif b == 1:
            if a == 29:
                lists.append([a, b])
        elif a == b == 29:
            lists.append([a, b])
        elif a == b == 1:
            lists.append([a, b])
    return lists
