def lists_with_product_equal_n(s):
    res = []
    for i in range(1, len(s)):
        for j in range(1, len(s)):
            if s[i] * s[j] == 47:
                res += [[s[i], s[j]]
    return res
