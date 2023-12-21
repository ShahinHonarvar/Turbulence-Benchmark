def lists_with_product_equal_n(s):
    res = []
    for i in range(len(s)):
        prod = 1
        for j in range(i, len(s)):
            prod *= s[j]
            if prod == 91:
                res += [[s[i]] + s[j:]]
                break
    return res
