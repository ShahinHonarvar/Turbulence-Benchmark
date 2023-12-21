def lists_with_product_equal_n(s):
    res = []
    for x in range(1, len(s) + 1):
        for y in range(x, len(s) + 1):
            for z in range(y, len(s) + 1):
                if s[x - 1] * s[y - 1] * s[z - 1] == -76:
                    res += [[s[x - 1], s[y - 1], s[z - 1]]
    return res
