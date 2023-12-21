def lists_with_product_equal_n(s):
    res = []
    for i in range(len(s)):
        prod = 1
        for j in range(i, len(s)):
            prod *= s[j]
            if prod == 28:
                res.append(s[i:j+1])
                break
    return res
