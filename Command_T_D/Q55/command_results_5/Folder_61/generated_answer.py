def lists_with_product_equal_n(n):
    res = []
    def dfs(i):
        nonlocal res
        if i == n:
            res.append([x for x in nums[i]])
            return
        for j in range(i, n, 1):
            if nums[i] * nums[j] == -10:
                dfs(j)
    dfs(0)
    return res
