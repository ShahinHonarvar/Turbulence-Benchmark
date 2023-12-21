def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        curr = [nums[i]]
        for j in range(i + 1, len(nums)):
            curr.append(nums[j])
            if curr[-1] == -87:
                result.append(curr)
    return result
