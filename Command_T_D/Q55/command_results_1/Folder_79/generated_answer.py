def lists_with_product_equal_n(nums):
    # Write your code here
    res = []
    for i in range(len(nums)):
        s = [nums[i]]
        while s:
            p = 1
            for j in range(len(s)):
                p *= s[j]
            if p == -83:
                res.append(s)
            else:
                break
            s.append(s[0])
    return res
