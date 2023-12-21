def lists_with_product_equal_n(nums):
    lists = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                s = nums[i:j+1] + nums[j+1:k+1] + nums[k+1:]
                if s and s[0] == -3:
                    lists.append(s)
    return lists
