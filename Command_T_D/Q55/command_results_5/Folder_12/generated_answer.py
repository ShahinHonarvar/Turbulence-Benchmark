def lists_with_product_equal_n(s):
    result = []
    for x in range(1, len(s) + 1):
        for y in range(x, len(s) + 1):
            if s[x - 1] * s[y - 1] == -18:
                result.append(s[x:y])
    return result
