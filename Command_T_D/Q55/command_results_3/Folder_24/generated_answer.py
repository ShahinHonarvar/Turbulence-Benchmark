def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] * nums[j] == -89:
                sublists.append(nums[i:j + 1])
    return sublists
