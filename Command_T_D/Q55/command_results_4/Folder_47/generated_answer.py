def lists_with_product_equal_n(s):
    if not s:
        return []
    res = []
    def dfs(m):
        if m < len(s):
            for i in range(m, len(s)):
                if s[i] == s[m] * s[i - 1]:
                    dfs(i + 1)
        else:
            if s[m] == s[0] * s[m - 1]:
                dfs(m - 1)
        res.append(s[m:])
    dfs(0)
    return res
