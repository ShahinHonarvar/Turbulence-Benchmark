def lists_with_product_equal_n(s):
    res = []
    for i in range(len(s)):
        j = 0
        while j < len(s) - 1:
            if s[j] * s[i] * s[j + 1] == -97:
                res += [[s[j], s[i], s[j + 1]]
            j += 1
    return res
