def lists_with_product_equal_n(s):
    res = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] * s[j] == -69:
                res += [[s[i], s[j]]
    return res
