def lists_with_product_equal_n(nums):
    res = []
    def dfs(i, j, num_set):
        if i == len(nums):
            res.append(num_set)
            return
        for j in range(i, len(nums)):
            if num_set.issubset(nums[j:]):
                dfs(i+1, j+1, num_set | nums[j:])
    dfs(0, 0, set())
    return res
