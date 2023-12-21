def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        curr = [nums[i]]
        for j in range(i + 1, len(nums)):
            curr.append(nums[j])
            if curr[-1] == curr[-2] and curr[-1] == -72:
                res += [[curr]]
                break
    return res
